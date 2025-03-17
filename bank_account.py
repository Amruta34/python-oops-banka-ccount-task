class BankAccount:
    total_acc = 0

    def __init__(self, acc_owner, balance=0):
        if not acc_owner:
            raise ValueError("Account Owner Name Cannot be Empty.")
        if not self._validate_amount(balance):
            raise ValueError("Initial balance is Invalid.")
        self.acc_owner = acc_owner
        self.balance = balance
        self.transactions = []
        BankAccount.total_acc +=1
        print(f"Account is created for {self.acc_owner}.")

    def deposit(self, amount):
        if self._validate_amount(amount):
            self.balance = self.balance+amount
            self.transactions.append(f"Deposited amount is ₹{amount}")
        else:
            print("The deposited amount is Invalid.")

    def withdraw(self, amount):
        if not self._validate_amount(amount) or amount > 60000:
            print("You entered an invalid withdrawal amount.")
            return
        if self.balance - amount < 0:
            print("There is insufficient amount in your bank account.")
            return
        
        self.balance -= (amount + 20)
        self.transactions.append(f"Withdraw Amount ₹{amount} and ₹20 fee")

    def transfer(self, recipient, amount):
        if not isinstance(recipient, BankAccount):
            print("This recipient is invalid.")
            return
        if not self._validate_amount(amount):
            print("The entered amount is invalid for transfer.")
            return
        if self.balance - amount < 0:
            print("You entered a transfer amount that is more than your bank balance.")
            return
        
        self.balance -= amount
        recipient.balance += amount
        self.transactions.append(f"Transferred Amount is: ₹{amount} to {recipient.acc_owner}")
        recipient.transactions.append(f"Received Amount is: ₹{amount} from {self.acc_owner}")

    def check_balance(self):
        print(f"The balance of {self.acc_owner} is: ₹{self.balance}.")

    def get_transaction_history(self):
        return self.transactions

    @classmethod
    def total_bank_accounts(cls):
        return cls.total_acc
    
    @staticmethod
    def _validate_amount(amount):
        return isinstance(amount, (int, float)) and amount > 0 and amount <= 60000

acc = BankAccount("Amruta Bhosale", 20000)
acc1 = BankAccount("Aniket Kalamkar", 10000)
acc2 = BankAccount("Shruti Chavan", 30000)
acc.deposit(10000)
acc1.transfer(acc, 19000)
acc1.withdraw(16000)
acc.check_balance()
acc1.check_balance()
acc2.check_balance()
print("Transaction History for Amruta Bhosale:", acc.get_transaction_history())
print("Transaction History for Aniket Kalamkar:", acc1.get_transaction_history())
print("Transaction History for Shruti Chavan:", acc2.get_transaction_history())
print("Total bank accounts:", BankAccount.total_bank_accounts())
