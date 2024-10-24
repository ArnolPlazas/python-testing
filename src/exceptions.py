class InsufficientFundsError(Exception):
    def __init__(self, message, amount):
        super().__init__(message)
        self.amount = amount

    def __str__(self):
        return f"{self.message} (Amount: {self.amount})"


class WithdrawalTimeRestrictionError(Exception):
    def __init__(self, message):
        super().__init__(message)


    def __str__(self):
        return f"{self.message}"