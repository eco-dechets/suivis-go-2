from repositories.database import DatabaseRepository
import streamlit_authenticator as stauth
import string
import random


class AuthRepository(DatabaseRepository):

    def __init__(self):
        super().__init__()

    def insert_user(self, username: str, password: str, email: str) -> int:
        """
        Insert a new row into the user table and retrieve the auto-incremented ID
        :param username: username of the user
        :param password: password of the user
        :param email: email of the user
        :param role: role of the user
        :return: id of the user
        """

        hashed_password = stauth.Hasher([password]).generate()[0]

        query = "INSERT INTO user (username, password, email) VALUES (%s, %s, %s)"
        values = (username, hashed_password, email)
        self.cursor.execute(query, values)
        self.connect.commit()
        return self.cursor.lastrowid

    def get_users(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def get_user(self, email: str) -> tuple:
        """
        Retrieve a user from the database
        :param email: email of the user
        :return: user
        """
        query = "SELECT * FROM user WHERE email = %s"
        values = (email,)
        self.cursor.execute(query, values)
        return self.cursor.fetchone()

    def reset_password(self, email: str, password: str) -> str:
        """
        Reset the password of a user
        :param email: email of the user
        :param password: new password
        :return: new password
        """
        hashed_password = stauth.Hasher([password]).generate()[0]
        query = "UPDATE user SET password = %s WHERE email = %s"
        values = (hashed_password, email)
        self.cursor.execute(query, values)
        self.connect.commit()
        return password

    def delete_user(self, email):
        self.cursor.execute("DELETE FROM users WHERE email = %s", (email,))
        self.connect.commit()

    def add_role_to_users(self):
        self.cursor.execute(
            "ALTER TABLE users ADD role VARCHAR(255) DEFAULT 'user'")
        self.connect.commit()
        print('Role added to users')

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
