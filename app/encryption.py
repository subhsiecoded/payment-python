import hashlib
import uuid
import random
import string

class Encryption:
    @staticmethod
    def hash_password(password):
        salt = uuid.uuid4().hex
        hashed_password = hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
        return hashed_password

    @staticmethod
    def check_password(stored_password, provided_password):
        password, salt = stored_password.split(':')
        return password == hashlib.sha256(salt.encode() + provided_password.encode()).hexdigest()

    @staticmethod
    def generate_secure_token():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=32))
