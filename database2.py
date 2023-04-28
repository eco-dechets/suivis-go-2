import streamlit_authenticator as stauth
import mysql.connector
import string
import random
import os
from dotenv import load_dotenv
# charger les variables d'environnement à partir d'un fichier .env
load_dotenv()


# load env variables


# get env variables
DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME = os.environ.get('DB_DATABASE')
# connexion à la base de données MySQL
mydb = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)


class Database2:
    # initialiser les variables de connexion à la base de données
    def __init__(self):
        self.cursor = mydb.cursor()
        self.connect = mydb
        self.migrate()
    # créer la  table users

    def migrate(self):
        self.__create_table_users()

    def __create_table_users(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, password VARCHAR(255), email VARCHAR(255) UNIQUE, name VARCHAR(255))")
        mydb.commit()
        print('Table users created')

    # insérer un nouveau user dans la table users
    def insert_user(self, password, email, name):
        hashed_password = stauth.Hasher([password]).generate()[0]
        print(hashed_password)
        self.cursor.execute("INSERT INTO users (password, email, name) VALUES (%s, %s, %s)",
                            (hashed_password, email, name))
        mydb.commit()
        print('User inserted')

    def get_user(self, email):
        self.cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        return self.cursor.fetchone()

    def get_users(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def reset_password(self, email, password):
        hashed_password = stauth.Hasher([password]).generate()[0]
        self.cursor.execute(
            "UPDATE users SET password = %s WHERE email = %s", (hashed_password, email))
        mydb.commit()
        return password

    def delete_user(self, email):
        self.cursor.execute("DELETE FROM users WHERE email = %s", (email,))
        mydb.commit()

    def add_role_to_users(self):
        self.cursor.execute(
            "ALTER TABLE users ADD role VARCHAR(255) DEFAULT 'user'")
        mydb.commit()
        print('Role added to users')




    
    def find_or_create(self, table, field, value, func = None):
        self.cursor.execute(f"SELECT id FROM {table} WHERE {field} = '{value}'")
        response = self.cursor.fetchone()
       
        if response:
            return response[0]
        else:
           return func()
    


    def insert_transaction_carburant(self,
                                     num_transaction=None,
                                     code_transaction=None,
                                     id_fournisseurs=None,
                                     id_station=None,
                                     id_site=None,
                                     id_produit=None,
                                     id_client=None,
                                     id_conducteur=None,
                                     id_vehicule=None,
                                     id_carte=None,
                                     id_ville=None,
                                     date_transaction=None,
                                     heure_transaction=None,
                                     num_facture=None,
                                     date_facture=None,
                                     unite=None,
                                     quantite=None,
                                     montant_ht=None,
                                     pu_ht=None,
                                     pu_ttc=None,
                                     montant_ttc=None,
                                     frais_service_ht=None,
                                     frais_service_ttc=None,
                                     kilometrage=None,
                                     consoL_au100=None,
                                     taux_tva=None,
                                     montant_tva=None,
                                     taux_remise=None,
                                     montant_remise=None,
                                     devise=None,
                                     etat=None,
                                     mention_complementaire=None,
                                     ):
        self.cursor.execute(
            "INSERT INTO transaction_carburant (num_transaction, code_transaction,id_fournisseurs,id_station, id_site,id_produit, id_client,  id_conducteur, id_vehicule,id_carte, id_ville, date_transaction,heure_transaction, num_facture,date_facture, unite,quantite, montant_ht, pu_ht, pu_ttc, montant_ttc,frais_service_ht,frais_service_ttc, kilometrage, consoL_au100, taux_tva, montant_tva, taux_remise, montant_remise,devise, etat, mention_complementaire) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
              (num_transaction, code_transaction,id_fournisseurs,id_station, id_site,id_produit, id_client,  id_conducteur, id_vehicule,id_carte, id_ville, date_transaction,heure_transaction, num_facture,date_facture, unite,quantite, montant_ht, pu_ht, pu_ttc, montant_ttc,frais_service_ht,frais_service_ttc, kilometrage, consoL_au100, taux_tva, montant_tva, taux_remise, montant_remise,devise, etat, mention_complementaire)
        )

    def test(self, id_carte):
        self.cursor.execute(
            "INSERT INTO transaction_carburant (id_carte) VALUES (%s)", (id_carte,))

    def get_transaction_carburant(self):
        self.cursor.execute("SELECT * FROM transaction_carburant")
        return self.cursor.fetchall()

    @staticmethod
    def generate_password(length=8):
        password = ''
        for i in range(length):
            password += random.choice(string.ascii_letters + string.digits)
        return password

    def login(self, email, password):
        try:
            hashed_password = stauth.Hasher([password]).generate()
            self.cursor.execute(
                "SELECT * FROM users WHERE email = %s AND password = %s", (email, hashed_password[0]))
            return self.cursor.fetchone()
        except:
            return None






