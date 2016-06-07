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


class SalariedEmployee(Employees):

    def __init__(self, employee_id, last_name, first_name, salary, commission_rate, weekly_dues):
        Employees.__init__(employee_id, last_name, first_name, weekly_dues)
        self.__salary = salary
        self.__commission_rate = commission_rate

    def set_salary(self, salary):
        self.__salary = salary

    def set_commission_rate(self, commission_rate):
        self.__commission_rate = commission_rate

    def get_salary(self, salary):
        return self.__salary

    def get_commission_rate(self, commission_rate):
        return self.__commission_rate


def main():
    maryj = SalariedEmployee("Smith", "Mary J")
    salary = "$65,000"
    commission_rate = "10%"

    print (maryj.get_full_name())
    print(salary.get_salary())
    print(commission_rate.get_commission_rate())

main()


