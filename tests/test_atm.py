import unittest
from concurrent.futures import ThreadPoolExecutor

from algo.atm import BankAccount


class TestAtm(unittest.TestCase):
    def test_single_withdrawal(self):
        account = BankAccount(1000)
        account.withdraw(300)
        self.assertEqual(account.balance, 700)

    def test_multiple_withdrawals(self):
        account = BankAccount(1000)

        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = [executor.submit(account.withdraw, 600) for _ in range(2)]

        for futures in futures:
            futures.result()

        self.assertEqual(account.balance, 400)


if __name__ == '__main__':
    unittest.main()
