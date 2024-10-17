import unittest
import os

from src.exceptions import InsufficientFundsError
from src.bank_account import BankAccount

class BankAccountTest(unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(balance=1000, log_file='transaction_log.txt')


    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)
    
    
    def _count_lines(self, filename):
        with open(filename, 'r') as f:
            return len(f.readlines())
    

    def test_deposit_increases_balance_by_deposit_amount(self):
        new_balance = self.account.deposit(500)
        # assert new_balance == 1500
        self.assertEqual(new_balance, 1500, 'The balance is not the same')
    

    def test_withdraw_decreases_balance_by_withdraw_amount(self):
        new_balance = self.account.withdraw(200)
        # assert new_balance == 800
        self.assertEqual(new_balance, 800, 'The balance is not the same')

    def test_get_balance_returns_current_balance(self):
        # assert self.account.get_balance() == 1000
        self.assertEqual(self.account.get_balance(), 1000)
    
    def test_deposit_logs_transaction(self):
        self.account.deposit(500)
        # assert os.path.exists('transaction_log.txt')
        self.assertTrue(os.path.exists('transaction_log.txt'))
    

    def test_withdraw_logs_each_transaction(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(500)
        assert self._count_lines(self.account.log_file) == 2
    

    def test_withdraw_raises_error_when_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsError):
            self.account.transfer(1001)


