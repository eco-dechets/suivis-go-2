from repositories.database import DatabaseRepository


class VehicleRepository(DatabaseRepository):

    def __init__(self):
        super().__init__()

    def insert_vehicle(self, registration: str) -> tuple:
        """
        Insert a vehicle into the database
        :param registration:
        :return: id of the vehicle
        """

        query = f"SELECT * FROM vehicule WHERE immatriculation = %s"
        values = (registration,)
        self.cursor.execute(query, values)
        row = self.cursor.fetchone()

        if row is None:
            query = f"INSERT INTO vehicule (immatriculation) VALUES (%s)"
            values = (registration,)
            self.cursor.execute(query, values)
            self.connect.commit()
        return row

    def get_vehicle_by_registration(self, registration: str) -> int:
        """
        Get a vehicle by registration
        :param registration:
        :return: id of the vehicle
        """
        self.cursor.execute("SELECT * FROM vehicule WHERE immatriculation = %s", (registration,))
        return self.cursor.fetchone()
