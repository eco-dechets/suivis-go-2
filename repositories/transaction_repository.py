from repositories.database import DatabaseRepository


class TransactionRepository(DatabaseRepository):

    def __init__(self):
        super().__init__()

    def insert_transaction(self, num: int = None, code: int = None, id_vendor: int = None, id_station: int = None,
                           id_site: int = None, id_product: int = None, id_vehicle: int = None, id_driver: int = None,
                           id_client: int = None, id_card: int = None, id_city: int = None, date: str = None,
                           hour: str = None, invoice: int = None, invoice_date: str = None,
                           quantity: float = None,
                           unit_price_ht: float = None, amount_ht: float = None, amount_ttc: float = None,
                           unit_price_ttc: float = None,
                           service_cost_ht: float = None, service_cost_ttc: float = None, kilometer: int = None,
                           consumption: float = None,
                           tva_rate: int = None, tva_amount: float = None, discount_rate: int = None,
                           discount_amount: float = None, status: str = None, complement: str = None) -> int:
        """
        Insert a new row into the transaction table and retrieve the auto-incremented ID
        :param num: number of the transaction
        :param code: code of the transaction
        :param id_vendor: id of the vendor
        :param id_station:  d of the station
        :param id_site: id of the site
        :param id_product: id of the product
        :param id_vehicle: id of the vehicle
        :param id_driver: id of the driver
        :param id_client:
        :param id_card:
        :param id_city:
        :param date: date of the transaction
        :param hour: hour of the transaction
        :param invoice: invoice number
        :param invoice_date: invoice date
        :param unity: unity of the fuel
        :param quantity:  quantity of the fuel
        :param unit_price_ht: unit price of the fuel
        :param amount_ht:
        :param amount_ttc:
        :param unit_price_ttc:
        :param service_cost_ht:
        :param service_cost_ttc:
        :param kilometer:
        :param consumption:
        :param tva_rate:
        :param tva_amount:
        :param discount_rate:
        :param discount_amount:
        :param status:
        :param complement:
        :return:
        """

        # get transaction with same date, carte and qauntity
        query = "SELECT * FROM transaction_carburant WHERE date_transaction = %s AND id_carte = %s AND quantite = %s"
        values = (date, id_card, quantity)
        self.cursor.execute(query, values)
        row = self.cursor.fetchone()

        print(row)

        if row is not None:
            query = "INSERT INTO transaction_carburant (num_transaction, code_transaction, id_fournisseurs, id_station, id_site, id_produit, id_vehicule, id_conducteur, id_client, id_carte, id_ville, date_transaction, heure_transaction, num_facture, date_facture, quantite, pu_ht, montant_ht, montant_ttc, pu_ttc, frais_service_ht, frais_service_ttc, kilometrage, consoL_au100, taux_tva, montant_tva, taux_remise, montant_remise, etat, mention_complementaire) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (
                num, code, id_vendor, id_station, id_site, id_product, id_vehicle, id_driver, id_client, id_card,
                id_city,
                date, hour, invoice, invoice_date, quantity, unit_price_ht, amount_ht, amount_ttc, unit_price_ttc,
                service_cost_ht, service_cost_ttc, kilometer, consumption, tva_rate, tva_amount, discount_rate,
                discount_amount, status, complement)
            self.cursor.execute(query, values)
            self.connect.commit()
        return row

    def __get_all_transactions(self) -> list:
        """
        Get all transactions
        :return: list of transactions
        """
        query = "SELECT * FROM transaction_carburant"
        self.cursor.execute(query)
        return self.cursor.fetchall()
