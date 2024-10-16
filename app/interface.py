from app.authentication import AuthenticationSystem
from app.transaction import Transaction
from app.gateway import PaymentGateway

class PaymentSystemInterface:
    def __init__(self):
        self.auth_system = AuthenticationSystem()
        self.gateway = PaymentGateway()
        self.active_user = None

    def start(self):
        while True:
            print("1. Create User")
            print("2. Login")
            print("3. Deposit Funds")
            print("4. Make Payment")
            print("5. View Balance")
            print("6. View Transactions")
            print("7. Process Transactions")
            print("8. Logout")
            print("9. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.create_user()
            elif choice == "2":
                self.login()
            elif choice == "3" and self.active_user:
                self.deposit()
            elif choice == "4" and self.active_user:
                self.make_payment()
            elif choice == "5" and self.active_user:
                self.view_balance()
            elif choice == "6" and self.active_user:
                self.view_transactions()
            elif choice == "7":
                self.process_transactions()
            elif choice == "8":
                self.logout()
            elif choice == "9":
                break
            else:
                print("Invalid option or not logged in")

    def create_user(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        self.auth_system.create_user(username, password)
        print("User created successfully")

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        user = self.auth_system.authenticate_user(username, password)
        if user:
            self.active_user = user
            print("Login successful")
        else:
            print("Authentication failed")

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.active_user.deposit(amount)
        print(f"${amount:.2f} deposited")

    def view_balance(self):
        balance = self.active_user.get_balance()
        print(f"Your balance: ${balance:.2f}")
    
    def make_payment(self):
        recipient_username = input("Enter recipient username: ")
        recipient = self.auth_system.get_user(recipient_username)
        if recipient:
            amount = float(input("Enter amount to pay: "))
            self.active_user.make_payment(amount, recipient)
            print(f"Paid ${amount:.2f} to {recipient_username}")
        else:
            print("Recipient not found")


    def view_balance(self):
        balance = self.active_user.get_balance()
        print(f"Your balance: ${balance:.2f}")

    def view_transactions(self):
        transactions = self.active_user.get_transactions()
        if transactions:
            for t in transactions:
                print(f"{t[1]} paid {t[2]} ${t[3]:.2f} on {t[4]}")
        else:
            print("No transactions found")

    def process_transactions(self):
        self.gateway.process_transactions()

    def logout(self):
        self.active_user = None
        print("Logged out")
