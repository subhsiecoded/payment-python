import unittest
from app.user import User

class TestUser(unittest.TestCase):
    def test_deposit(self):
        user = User('testuser', 'testpassword')
        user.deposit(100)
        self.assertEqual(user.get_balance(), 100)

    def test_make_payment(self):
        user1 = User('user1', 'pass1')
        user2 = User('user2', 'pass2')
        user1.deposit(100)
        user1.make_payment(50, user2)
        self.assertEqual(user1.get_balance(), 50)
        self.assertEqual(user2.get_balance(), 50)
