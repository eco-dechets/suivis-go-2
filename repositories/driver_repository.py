from repositories.database import DatabaseRepository


class DriverRepository(DatabaseRepository):

    def __init__(self):
        super().__init__()

    def insert_driver(self, name: str = None, code: int = None) -> tuple:
        """
        Insert a new conductor in the database
        :param name: name of the conductor
        :param code: code of the conductor
        :return:
        """

        query = "SELECT * FROM conducteur WHERE code = %s"
        values = (code,)
        self.cursor.execute(query, values)
        row = self.cursor.fetchone()

        if row is None:
            query = "INSERT INTO conducteur (nom, code) VALUES (%s, %s)"
            values = (name, code)
            self.cursor.execute(query, values)
            self.connect.commit()
        return row

    def get_conductor_by_code(self, code: int) -> tuple:
        """
        Get a conductor by its code
        :param code: code of the conductor
        :return:
        """
        self.cursor.execute("SELECT * FROM conductor WHERE code = %s", (code,))
        return self.cursor.fetchone()

    def get_conductor_by_name(self, name: str) -> tuple:
        """
        Get a conductor by its name
        :param name: name of the conductor
        :return:
        """
        self.cursor.execute("SELECT * FROM conductor WHERE name = %s", (name,))
        return self.cursor.fetchone()
