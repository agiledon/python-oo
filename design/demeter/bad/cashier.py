
class NotEnoughMoneyError(RuntimeError):
    pass


class Cashier(object):
    def charge(self, customer, payment):
        wallet = customer.wallet
        if wallet.get_total_money() >= payment:
            wallet.subtract_money(payment)
        else:
            raise NotEnoughMoneyError()

