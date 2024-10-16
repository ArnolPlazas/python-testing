class BankAccount:
    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction("created account")


    def _log_transaction(self, message):
        if self.log_file:
        # abre el archivo en modo append
            with open(self.log_file,"a") as f:
                f.write(f"{message}\n")


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Deposited {amount}. New balance: {self.balance}")
        return self.balance


    def withdraw(self, amount):
        if amount > 0 and amount < self.balance:
            self.balance -= amount
            self._log_transaction(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            self._log_transaction(f"this withdraw is not posible for this amount: {amount}")
        return self.balance


    def get_balance(self):
        self._log_transaction(f"Checked balance. Current balance: {self.balance}")
        return self.balance
    

    def transfer(self, amount):
        if self.balance < amount:
            self._log_transaction(f"this transfer is not posible for this amount: {amount}")
            raise 'insufficient balance'
        self.balance -= amount
        return self.balance