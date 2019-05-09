class NotEnoughMoneyError(RuntimeError):
    pass


class Customer:
    def __init(self, first_name, last_name, wallet):
        self.first_name = first_name
        self.last_name = last_name
        self.wallet = wallet

    def pay(self, payment):
        if self.wallet.get_total_money() >= payment:
            self.wallet.subtract_money(payment)
        else:
            raise NotEnoughMoneyError()
