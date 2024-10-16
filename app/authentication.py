from app.encryption import Encryption
from app.db import Database
from app.user import User

class AuthenticationSystem:
    def __init__(self):
        self.db = Database()

    def create_user(self, username, password):
        hashed_password = Encryption.hash_password(password)
        self.db.execute(
            "INSERT INTO users (username, password, balance) VALUES (%s, %s, 0)",
            (username, hashed_password)
        )

    def authenticate_user(self, username, password):
        user = self.db.fetchone("SELECT * FROM users WHERE username = %s", (username,))
        if user and Encryption.check_password(user[1], password):
            return User(username=user[0], password=user[1], balance=user[2])
        return None

    def get_user(self, username):
        user_data = self.db.fetchone("SELECT * FROM users WHERE username = %s", (username,))
        if user_data:
            return User(username=user_data[0], password=user_data[1], balance=user_data[2])
        return None
