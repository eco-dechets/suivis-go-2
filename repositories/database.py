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


class DatabaseRepository:
    def __init__(self):
        self.cursor = mydb.cursor(buffered=True)
        self.connect = mydb

    def find_or_create(self, table: str, field: str, value: [str, int], func) -> tuple:
        """
        Find a row in a table or create it if it doesn't exist
        :param table: table name
        :param field: field name
        :param value: field value
        :return: row
        """
        query = f"SELECT * FROM {table} WHERE {field} = %s"
        values = (value,)
        self.cursor.execute(query, values)
        row = self.cursor.fetchone()
        if row is None:
            # query = f"INSERT INTO {table} ({field}) VALUES (%s)"
            # values = (value,)
            # self.cursor.execute(query, values)
            # self.connect.commit()
            # row = self.cursor.fetchone()
            row = func()
        return row
