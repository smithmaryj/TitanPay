from accounting.employee import Employee
from accounting.receipts import Receipt
from accounting.direct_deposit_payment import DirectDepositPayment
from accounting.mail_payment import MailPayment
from accounting.pick_up_payment import PickUpPayment

class SalariedEmployee(Employee):

    # the __init__ method accepts the arguments for the general employee information and the
    # specific salaried employee information like employee id, full name, and weekly dues to
    # the union services. It initializes the data attributes with these values
    def __init__(self, id, last, first, salary, commiss_rate, dues, pay, street_address, city, state, zip):
        # Call the superclass's __init__method and pass the arguments necessary for the
        # general employee; self is also passed as an argument.
        Employee.__init__(self, id, last, first, salary, commiss_rate, dues, pay, street_address, city, state, zip)

        # initializes the __yearly_salary,  attribute
        self.__yearly_salary = float(salary)
        self.__commission_rate = float(commiss_rate) / 100
        self.__receipts = []

    def create_receipt(self, id, last, item, units, unit_cost, total):
        receipt = Receipt(id, last, item, units, unit_cost, total)
        self.__receipts.append(receipt)
        return

    def calculate_pay(self):
        pay_amt = 0
        for i in self.__receipts:
            pay_amt += i.get_pay_date() * self.__commission_rate

            pay_amt += i.self.__yearly_salary / 12
            dues = Employee.get_dues(self)
            pay_amt == float(dues)


            full_name = Employee.get_full_name(self)
            if Employee.get_pay(self) == "MA":
                full_address = Employee.get_full_address(self)
                mailpay = MailPayment(pay_amt, full_name, full_address)
                output = mailpay.get_output()

            elif Employee.get_pay(self) == "PU":
                pickuppay = PickUpPayment(pay_amt, full_name)
                output = pickuppay.get_output()

            else:
                Employee.get_pay(self) == "DD"
                ddeposit = DirectDepositPayment(total_pay, full_name)
                output = ddeposit.get_output()

            return output



