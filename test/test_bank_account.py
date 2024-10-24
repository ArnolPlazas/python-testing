import unittest
import os
from unittest.mock import patch

from src.exceptions import InsufficientFundsError, WithdrawalTimeRestrictionError
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
    
    @patch("src.bank_account.datetime")
    def test_withdraw_during_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        new_balance = self.account.withdraw(100)
        self.assertEqual(new_balance, 900)
    

    @patch("src.bank_account.datetime")
    def test_withdraw_during_no_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 7
        
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)
    

    @patch("src.bank_account.datetime")
    def test_withdraw_during_bussines_days(self, mock_datetime):
        mock_datetime.now.return_value.weekday.return_value = 3
        mock_datetime.now.return_value.hour = 8
        new_balance = self.account.withdraw(100)
        self.assertEqual(new_balance, 900)
    
    
    @patch("src.bank_account.datetime")
    def test_withdraw_during_no_bussines_days(self, mock_datetime):
        mock_datetime.now.return_value.weekday.return_value = 6
        mock_datetime.now.return_value.hour = 8
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)
    

    def test_deposit_several_amounts(self):
        
        test_cases = [
            {"amount": 100, "expected": 1100},
            {"amount": 3000, "expected": 4000},
            {"amount": 4500, "expected": 5500},
        ]

        for case in test_cases:
            with self.subTest(case=case):
                self.account = BankAccount(balance=1000, log_file='transaction_log.txt')
                new_balance = self.account.deposit(case["amount"])
                self.assertEqual(new_balance, case["expected"])



