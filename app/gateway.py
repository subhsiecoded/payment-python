from collections import deque

class PaymentGateway:
    def __init__(self):
        self.transaction_queue = deque()

    def add_transaction(self, transaction):
        self.transaction_queue.append(transaction)

    def process_transactions(self):
        while self.transaction_queue:
            transaction = self.transaction_queue.popleft()
            print(f"Processing {transaction}")
