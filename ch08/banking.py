class Teller:
    def deposit(self, amount, account):
        account.deposit(amount)


class CorruptTeller(Teller):  # <1>
    def __init__(self):
        self.coffers = 0

    def deposit(self, amount, account):  # <2>
        self.coffers += amount * 0.01  # <3>
        super().deposit(amount * 0.99, account)  # <4>
