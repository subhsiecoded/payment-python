from app.encryption import Encryption

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.transaction_id = Encryption.generate_secure_token()

    def __repr__(self):
        return f"{self.sender} paid {self.receiver} ${self.amount:.2f} | ID: {self.transaction_id}"
