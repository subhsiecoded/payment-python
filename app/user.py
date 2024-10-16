from app.encryption import Encryption
from app.db import Database

class User:
    def __init__(self, username, password, balance=0.0):
        self.username = username
        self.password = password
        self.balance = balance
        self.db = Database()

    def get_balance(self):
        user_data = self.db.fetchone(
            "SELECT balance FROM users WHERE username = %s", 
            (self.username,)
        )
        if user_data:
            return user_data[0]
        return 0.0

    def deposit(self, amount):
        self.balance += amount
        self.db.execute(
            "UPDATE users SET balance = %s WHERE username = %s",
            (self.balance, self.username)
        )

    def save_to_db(self):
        self.db.execute(
            "INSERT INTO users (username, password, balance) VALUES (%s, %s, %s)",
            (self.username, self.password, self.balance)
        )


    def make_payment(self, amount, recipient):
        if self.balance >= amount:
            self.balance -= amount
            recipient.receive_payment(amount, self.username)
            self.db.execute(
                "UPDATE users SET balance = %s WHERE username = %s",
                (self.balance, self.username)
            )
            recipient.update_balance_in_db()
            self.db.execute(
                "INSERT INTO transactions (sender, receiver, amount) VALUES (%s, %s, %s)",
                (self.username, recipient.username, amount)
            )
        else:
            raise ValueError('Insufficient funds')

    def update_balance_in_db(self):
        self.db.execute(
            "UPDATE users SET balance = %s WHERE username = %s",
            (self.balance, self.username)
        )

    def receive_payment(self, amount, sender):
        self.balance += amount
        self.db.execute(
            "UPDATE users SET balance = %s WHERE username = %s",
            (self.balance, self.username)
        )

    def get_transactions(self):
        return self.db.fetchall(
            "SELECT * FROM transactions WHERE sender = %s OR receiver = %s", 
            (self.username, self.username)
        )
