from repositories.database import DatabaseRepository


class ProductRepository(DatabaseRepository):

    def __init__(self):
        super().__init__()

    def insert_product(self, code: int = None, name: str = None, group: str = None) -> tuple:
        """
        Insert a product into the database
        :param code:
        :param name:
        :param group:
        :return:
        """

        query = "SELECT * FROM produit WHERE libelle_article = %s"
        values = (name,)
        self.cursor.execute(query, values)
        row = self.cursor.fetchone()

        if row is None:
            query = "INSERT INTO produit (code_article, libelle_article, groupe_produit) VALUES (%s, %s, %s)"
            values = (code, name, group)
            self.cursor.execute(query, values)
            self.connect.commit()
        return row

    def get_product_by_name(self, name: str) -> int:
        """
        Get a product by name
        :param name:
        :return:
        """
        self.cursor.execute("SELECT * FROM produit WHERE libelle_article = %s", (name,))
        return self.cursor.fetchone()
