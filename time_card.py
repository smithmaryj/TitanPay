import Employees

class TimeCard(Employees.HourlyEmployee):
    def __init__(self, date, time, clock_in, clock_out, total_worked):
        self.__date = date
        self.__time = time
        self.__clock_in = " "
        self.__clock_out = " "
        self.__total_worked = " "
        self.__hourly_rate = " "
        self.__calculate_daily_pay_rate = " "

    def get_date(self):
        return self.__date

    def get_start_time(self):
        return self.__clock_in

    def get_end_time(self):
        return self.__clock_out

    def get_total_worked(self):
        return self.__total_worked

    def get_hourly_rate(self):
        return self.__hourly_rate

    def get_calculate_daily_pay_rate(self):
        return self.__calculate_daily_pay_rate

    def set_date(self, date):
        self.__date = date

    def set_start_time(self, clock_in):
        self.__clock_in = clock_in

    def set__clock_out(self, clock_out):
        self.__clock_out = clock_out

    def set_total_worked(self, total_worked):
        self.__total_worked = total_worked

    def set_hourly_rate(self, hourly_rate):
        self.__hourly_rate = hourly_rate

    def set_calculate_daily_pay_rate(self, calculate_daily_pay_rate):
        self.__calculate_daily_pay_rate = calculate_daily_pay_rate

        if  self.__total_worked <= 8:
            self.__total_worked = (self.__total_worked * 1.50)
        else:
            timecard_total_worked.get_total_worked = 8 * 1.50 + (self.total_worked(" ") - 8) * (1.5 * timecard_rate.get_rate)

if __name__ == "__main__":
    timecard_total_worked = TimeCard(' ', ' ', ' ', ' ', ' ' )
    timecard_hourly_rate = TimeCard(' ', ' ', ' ', ' ', ' ' )

    timecard_total_worked.set_total_worked("40 hours")
    timecard_hourly_rate.set_hourly_rate("$20.00")
    print("Calculated Pay Rate: ", timecard_total_worked.get_total_worked(), timecard_rate.get_rate())

class AddTimeCard(object):
    def __init__(self, employee_id, date, hours):
        self.employee_id = employee_id
        self.date = date
        self.hours = hours


