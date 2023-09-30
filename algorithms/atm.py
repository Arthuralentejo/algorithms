import threading


class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()

    def withdraw(self, amount):
        with self.lock:
            if amount <= 0:
                print('Invalid amount')
                return

            if self.balance < amount:
                print('Insufficient funds')
                return

            print(f"Withdrawal of R${amount} successful")
            self.balance -= amount


def withdraw_from_account(account: BankAccount, amount: int, account_holder: str):
    print(f"{account_holder} is trying to withdraw ${amount}")
    account.withdraw(amount)


if __name__ == '__main__':
    ini_balance = 1000
    acc = BankAccount(ini_balance)

    person1 = threading.Thread(target=withdraw_from_account, args=(acc, 600, 'João'))
    person2 = threading.Thread(target=withdraw_from_account, args=(acc, 500, 'Maria'))

    person1.start()
    person2.start()

    person1.join()
    person2.join()

    print(f"Final balance: ${acc.balance}")
