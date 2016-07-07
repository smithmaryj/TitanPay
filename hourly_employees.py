from accounting.employee import Employee
from accounting.timecards import TimeCards
from accounting.direct_deposit_payment import DirectDepositPayment
from accounting.mail_payment import MailPayment
from accounting.pick_up_payment import PickUpPayment


# The Type of Employee represents that of a hourly paid one;
# it is a subclass of the Employee class.
class HourlyEmployee(Employee):

    # the __init__ method accepts the arguments for the general employee information and the
    # specific salaried employee information like employee id, full name, and weekly dues to
    # the union services. It initializes the data attributes with these values
    def __init__(self, id, last, first, hourly_rate, dues, pay, street_address, city, state, zip):
        # Call the superclass's __init__method and pass the arguments necessary for the
        # general employee; self is also passed as an argument.
        Employee.__init__(self, id, last, first, hourly_rate, dues, pay, street_address, city, state, zip)

        # initializes the __hourly_rate attribute
        self.__hourly_rate = hourly_rate
        self.__timeCards = []

    def clock_in(self, timecard_date, start_time):
        end_time = ""
        timecard = TimeCards(timecard_date, start_time, end_time)
        self.__timeCards.append(timecard)

    def clock_out(self, timecard_date, end_time):
        end_time = ""
        timecard = TimeCards(timecard_date, start_time, end_time)
        self.__timeCards.append(timecard)
        for i in self.__timeCards:
            if i.get_date() == timecard_date:
                i.set_end_time(end_time)

    def calculate_daily_pay_rate(self):

        total_pay = 0
        for timecard in self.__timeCards:
            total_pay += timecard.calculate_daily_pay_rate(self.__hourly_rate)

        if total_pay > 0:
            dues = float(Employee.get_dues(self))
            total_pay == dues
        else:
            return -1

        full_name = Employee.get_full_name(self)
        self.get_pay().pay(total_pay)

        if Employee.get_pay(self) == "MA":
            full_address = Employee.get_full_address(self)
            mailpay = MailPayment(total_pay, full_name, full_address)
            output = mailpay.get_output()

        elif Employee.get_pay(self) == "PU":
            pickuppay = PickUpPayment(total_pay, full_name)
            output = pickuppay.get_output()

        else:
            Employee.get_pay(self) == "DD"
            ddeposit = DirectDepositPayment(total_pay, full_name)
            output = ddeposit.get_output()

