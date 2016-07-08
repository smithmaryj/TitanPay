from accounting.employee import Employee
from accounting.timecards import TimeCards
from accounting.direct_deposit_payment import DirectDepositPayment

class TimeCards:
    def __init__(self, timecard_date, start_time, end_time):
        class TimeCard:

            def __init__(self):
                self.__date = " "
                self.__start_time = " "
                self.__end_time = " "
                self.__total_worked = " "
                self.__rate = " "
                self.__calculate_daily_pay_rate = " "

            def get_date(self):
                return self.__date

            def get_start_time(self):
                return self.__start_time

            def get_end_time(self):
                return self.__end_time

            def get_total_worked(self):
                return self.__total_worked

            def get_rate(self):
                return self.__rate

            def get_calculate_daily_pay_rate(self):
                return self.__calculate_daily_pay_rate

            def set_date(self, date):
                self.__date = date

            def set_start_time(self, start_time):
                self.__start_time = start_time

            def set_end_time(self, end_time):
                self.__end_time = end_time

            def set_total_worked(self, total_worked):
                self.__total_worked = total_worked

            def set_rate(self, rate):
                self.__rate = rate

            def set_calculate_daily_pay_rate(self, calculate_daily_pay_rate):
                self.__calculate_daily_pay_rate = calculate_daily_pay_rate

                if self.__total_worked <= 8:
                    self.__total_worked = (self.__total_worked * 1.50)
                else:
                    timecard_total_worked.get_total_worked = 8 * 1.50 + (self.total_worked(" ") - 8) * (
                    1.5 * timecard_rate.get_rate)



