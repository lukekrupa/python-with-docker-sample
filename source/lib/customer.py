class Customer(object):

    def __init__(self, name, balance = 0.0):
        self.name = name
        self.balance = balance

    def set_balance(self, balance = 0.0):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise RuntimeError('Cannot withdraw more than available balance!')

        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        if amount < 0.0:
            raise RuntimeError('Cannot deposit less than 0.0!')

        self.balance += amount
        return self.balance