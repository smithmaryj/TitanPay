from accounting.payment_method import PaymentMethod


class MailPayment(PaymentMethod):
    def __init__(self, pay_amt, name, address):
        PaymentMethod.__init__(self)
        self.pay_amt = pay_amt
        self.name = name
        self.address = address

    def get_output(self):
        output = "Mailing a check for $" + str(format(self.__pay_amt, ',.2f')) + " to " + self.__address \
                 + " for " + self.__name
        return output


class PickUpPayment:
    def __init__(self, pay_amt, full_name):
        PaymentMethod.__init__(self)
        self.pay_amt = pay_amt
        self.full_name = full_name

    def get_output(self):
        output = "A check for $" + str(format(self.__pay_amt, ',.2f')) + " for " + self.__full_name \
                 + " is waiting at the PostMaster"
        return output