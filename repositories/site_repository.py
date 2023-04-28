from repositories.database import DatabaseRepository


class SiteRepository(DatabaseRepository):

    def __init__(self):
        super().__init__()

    def insert_site(self, num: int, name: str = None) -> tuple:
        """
        Insert a site into the database
        :param num:
        :param name:
        :return:
        """

        query = "SELECT * FROM site WHERE num = %s"
        values = (num,)
        self.cursor.execute(query, values)
        row = self.cursor.fetchone()

        if row is None:
            query = "INSERT INTO site (num, nom) VALUES (%s, %s)"
            values = (num, name)
            self.cursor.execute(query, values)
            self.connect.commit()
        return row

    def get_site_by_num(self, num: int) -> int:
        """
        Get a site by num
        :param num:
        :return:
        """
        self.cursor.execute("SELECT * FROM site WHERE num = %s", (num,))
        return self.cursor.fetchone()
