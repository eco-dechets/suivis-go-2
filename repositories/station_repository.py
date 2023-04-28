from repositories.database import DatabaseRepository


class StationRepository(DatabaseRepository):

    def __init__(self):
        super().__init__()

    def insert_station(self, num: int, name: str, ref: int, recu: str) -> tuple:
        """
        Insert a station into the database
        :param num: numero de la station
        :param name: nom de la station
        :param ref: reference de saisie
        :param recu: bon enlevement
        :return:
        """

        query = "SELECT * FROM station WHERE nom = %s"
        values = (name,)
        self.cursor.execute(query, values)
        row = self.cursor.fetchone()

        if row is None:
            query = "INSERT INTO station (num, nom, ref_saisie, bon_enlevement) VALUES (%s, %s, %s, %s)"
            values = (num, name, ref, recu)
            self.cursor.execute(query, values)
            self.connect.commit()
        return row

    def __get_station_by_num(self, num: int) -> int:
        """
        Get a station by num
        :param num:
        :return:
        """
        self.cursor.execute("SELECT * FROM station WHERE num = %s", (num,))
        return self.cursor.fetchone()

    def __get_station_by_name(self, name: str) -> int:
        """
        Get a station by name
        :param name:
        :return:
        """
        self.cursor.execute("SELECT * FROM station WHERE nom = %s", (name,))
        return self.cursor.fetchone()
