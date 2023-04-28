from repositories.database import DatabaseRepository


class CardRepository(DatabaseRepository):

    def __init__(self):
        super().__init__()
        self.cursor = self.cursor

    def insert_card(self, num, nom: str = None, extra_nom: str = None, nature: str = None, rang: int = None,
                    text_additive: str = None) -> tuple:
        """
        Insert a new card in the database
        :param num: numéro de la carte
        :param nom: nom de la carte
        :param extra_nom: nom supplémentaire de la carte
        :param nature: nature de la carte
        :param rang:
        :param text_additive:
        :return:
        """


        query = "SELECT * FROM carte WHERE num = %s"
        values = (num,)
        self.cursor.execute(query, values)
        row = self.cursor.fetchone()

        if row is None:
            query = "INSERT INTO carte (num, nom, extra_nom, nature, rang, texte_additif) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (num, nom, extra_nom, nature, rang, text_additive)
            self.cursor.execute(query, values)
            self.connect.commit()
            row = self.cursor.lastrowid

        return row

    def __get_card_by_id(self, card_id: int) -> tuple:
        """
        Get a card by its id
        :param card_id: id of the card
        :return:
        """
        self.cursor.execute("SELECT * FROM carte WHERE id = %s", (card_id,))
        return self.cursor.fetchone()

    def __get_card_by_num(self, num: int) -> tuple:
        """
        Get a card by its number
        :param num: number of the card
        :return:
        """
        self.cursor.execute("SELECT * FROM carte WHERE num = %s", (num,))
        return self.cursor.fetchone()
