import unittest
from app.gateway import PaymentGateway
from app.transaction import Transaction

class TestPaymentGateway(unittest.TestCase):
    def test_transaction_queue(self):
        gateway = PaymentGateway()
        transaction = Transaction('alice', 'bob', 100)
        gateway.add_transaction(transaction)
        self.assertEqual(len(gateway.transaction_queue), 1)
