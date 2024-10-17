import unittest

from test_bank_account import BankAccountTest

def bank_account_suite():
    suite = unittest.TestSuite() # create a suite
    suite.addTest(BankAccountTest("test_deposit")) # add a test in a suite
    suite.addTest(BankAccountTest("test_withdraw")) # add a test in a suite
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(bank_account_suite())


