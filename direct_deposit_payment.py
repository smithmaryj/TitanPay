from accounting.bank_account import Account
from accounting.payment_method import PaymentMethod


class DirectDepositPayment(PaymentMethod):
    def __init__(self, pay_amt, full_name):
        PaymentMethod.__init__(self)
        self.pay_amt = pay_amt
        self.full_name = full_name

    def pay(self, pay_amt):
       bank_account = Account("Bank of America", "001134567", "456456456456")
       output = bank_account.deposit(self.pay_amt, self.full_name)
       return output