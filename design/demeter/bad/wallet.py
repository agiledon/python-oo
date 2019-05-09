class Wallet:
    def __init__(self, value):
        self.value = value

    def get_total_money(self):
        return self.value

    def add_money(self, deposit):
        self.value += deposit

    def subtract_money(self, debit):
        self.value -= debit
