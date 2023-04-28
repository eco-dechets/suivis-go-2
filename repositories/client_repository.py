from repositories.database import DatabaseRepository


class ClientRepository(DatabaseRepository):

    def __init__(self):
        super().__init__()

    def insert_client(self, nom: str, code: int) -> tuple:
        """
        Insert a new client in the database
        :param nom: nom du client
        :param code: code du client
        :return:
        """

        query = "SELECT * FROM client WHERE nom = %s"
        values = (nom,)
        self.cursor.execute(query, values)
        row = self.cursor.fetchone()

        if row is None:
            query = "INSERT INTO client (nom, code) VALUES (%s, %s)"
            values = (nom, code)
            self.cursor.execute(query, values)
            self.connect.commit()
        return row

    def __get_client_by_id(self, client_id: int) -> tuple:
        """
        Get a client by its id
        :param client_id: id of the client
        :return:
        """
        self.cursor.execute("SELECT * FROM client WHERE id = %s", (client_id,))
        return self.cursor.fetchone()

    def __get_client_by_code(self, code: int) -> tuple:
        """
        Get a client by its code
        :param code: code of the client
        :return:
        """
        self.cursor.execute("SELECT * FROM client WHERE code = %s", (code,))
        return self.cursor.fetchone()

    def __get_client_by_nom(self, nom: str) -> tuple:
        """
        Get a client by its name
        :param nom: name of the client
        :return:
        """
        self.cursor.execute("SELECT * FROM client WHERE nom = %s", (nom,))
        return self.cursor.fetchone()
