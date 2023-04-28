from repositories.database import DatabaseRepository


class VendorRepository(DatabaseRepository):

    def __init__(self):
        super().__init__()

    def insert_vendor(self, name: str, partner_code: int = None, partner_name: str= None) -> tuple:
        """
        Insert a vendor into the database
        :param name: vendor name
        :param partner_code: vendor partner code
        :param partner_name: vendor partner name
        :return: vendor id
        """

        query = "SELECT id FROM fournisseurs WHERE nom = %s"
        values = (name,)
        self.cursor.execute(query, values)
        row = self.cursor.fetchone()

        if row is None:
            query = "INSERT INTO fournisseurs (nom, code_partenaire, partenaire) VALUES (%s, %s, %s)"
            values = (name, partner_code, partner_name)
            self.cursor.execute(query, values)
            self.connect.commit()
        return row

    def get_vendor_by_name(self, name: str) -> int:
        """
        Get a vendor by name
        :param name: vendor name
        :return: vendor id
        """
        self.cursor.execute("SELECT id FROM fournisseur WHERE nom = %s", (name,))
        return self.cursor.fetchone()
