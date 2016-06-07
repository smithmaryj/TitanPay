class Employees:
    def __init__(self, employee_id, last_name, first_name, weekly_dues):
        self.__employee_id = employee_id
        self.__last_name = last_name
        self.__first_name = first_name
        self.__weekly_dues = weekly_dues

    def get_employee_id(self):
        return self.__employee_id

    def get_full_name(self):
        return self.__last_name + " " + self.__first_name

    def get_weekly_dues(self):
        return self.__weekly_dues


class HourlyEmployee(Employees):

    def __init__(self, employee_id, last_name, first_name, hourly_rate, weekly_dues):
        Employees.__init__(employee_id, last_name, first_name, weekly_dues)
        self.__hourly_rate = hourly_rate


    def set_hourly_rate(self, hourly_rate):
        self.__hourly_rate = hourly_rate

    def get_hourly_rate(self, hourly_rate):
        return self.__hourly_rate
def main():
    adrian = HourlyEmployee("Tillman", "Adrian")
    hourly_rate = "$25/hr"

    print(adrian.get_full_name())
    print(hourly_rate.get_hourly_rate())

