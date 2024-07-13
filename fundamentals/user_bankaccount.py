class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self, user):
        print(f"User: {user.name}, Balance: ${self.balance} {user.email}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self
    
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0.02, 0)

    def create_account(self, account_name, int_rate, balance):
        self.accounts[account_name] = BankAccount(int_rate, balance)
        return self

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info(self)
        return self
    
user1 = User("John", "john@gmail.com")
user2 = User("Jane", "jane@gmail.com.com")

user1.make_deposit(1000).make_deposit(500).make_deposit(200).make_withdrawal(400).display_user_balance()
user2.make_deposit(300).make_deposit(200).make_withdrawal(100).make_withdrawal(50).make_withdrawal(75).make_withdrawal(25).display_user_balance()