class BankingManagementSystem:
    def __init__(self):
        # Dictionary to store multiple users with their balances
        self.users = {}

    def add_user(self, name, initial_balance=0):
        """Add a new user with a default or specified initial balance."""
        if name in self.users:
            print(f"User '{name}' already exists.")
        elif initial_balance < 0:
            print("Initial balance cannot be negative.")
        else:
            self.users[name] = initial_balance
            print(f"User '{name}' added with an initial balance of ${initial_balance:.2f}.")

    def deposit(self, name, amount):
        """Deposit an amount to the specified user's account."""
        if name not in self.users:
            print(f"User '{name}' not found.")
        elif amount <= 0:
            print("Deposit amount must be greater than 0.")
        else:
            self.users[name] += amount
            print(f"Deposited ${amount:.2f} to '{name}'. Updated Balance: ${self.users[name]:.2f}")

    def withdraw(self, name, amount):
        """Withdraw an amount from the specified user's account."""
        if name not in self.users:
            print(f"User '{name}' not found.")
        elif amount > self.users[name]:
            print(f"Insufficient balance for '{name}'. Available Balance: ${self.users[name]:.2f}")
        elif amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        else:
            self.users[name] -= amount
            print(f"Withdrew ${amount:.2f} from '{name}'. Updated Balance: ${self.users[name]:.2f}")

    def get_balance(self, name):
        """Check the current balance of the specified user."""
        if name not in self.users:
            print(f"User '{name}' not found.")
        else:
            print(f"Holder Name: {name}")
            print(f"Current Balance: ${self.users[name]:.2f}")

    def list_users(self):
        """List all users and their balances."""
        if not self.users:
            print("No users in the system.")
        else:
            print("\n--- User List ---")
            for name, balance in self.users.items():
                print(f"Name: {name}, Balance: ${balance:.2f}")


# Main Program
def main():
    # Create an instance of BankingManagementSystem
    bank = BankingManagementSystem()

    while True:
        print("\n--- Banking Management System ---")
        print("1. Add User")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Balance Inquiry")
        print("5. List All Users")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter the name of the user: ")
            initial_balance = float(input("Enter initial balance (default is 0): ") or 0)
            bank.add_user(name, initial_balance)
        elif choice == '2':
            name = input("Enter the name of the user: ")
            amount = float(input("Enter amount to deposit: "))
            bank.deposit(name, amount)
        elif choice == '3':
            name = input("Enter the name of the user: ")
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw(name, amount)
        elif choice == '4':
            name = input("Enter the name of the user: ")
            bank.get_balance(name)
        elif choice == '5':
            bank.list_users()
        elif choice == '0':
            print("Exiting the system. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main program
if __name__ == "__main__":
    main()
