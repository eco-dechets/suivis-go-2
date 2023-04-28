from repositories.database import DatabaseRepository


class CityRepository(DatabaseRepository):

    def __init__(self):
        super().__init__()

    def insert_city(self, name, post_code, department=None) -> tuple:
        """
        Insert a new row into the city table and return the auto-incremented ID
        :param name: city name
        :param post_code: city post code
        :param department: city department
        :return: city ID
        """

        query = "SELECT * FROM ville WHERE nom = '{}'".format(name)
        self.cursor.execute(query)
        row = self.cursor.fetchone()

        if row is None:
            query = "INSERT INTO ville (nom, code_postal, departement) VALUES ('{}', '{}', '{}')".format(name,
                                                                                                         post_code,
                                                                                                         department)
            self.cursor.execute(query)
            self.connect.commit()
        return row

    def __get_city_by_name(self, name):
        """
        Retrieve a city by its name
        :param name: city name
        :return: city ID
        """
        query = "SELECT id FROM ville WHERE nom = '{}'".format(name)
        self.cursor.execute(query)
        return self.cursor.fetchone()
