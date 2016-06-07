# Mary J Smith, 2295760
# The Employees class represents a superclass of general employee information needed for Titan Payroll to process

class Employees:
    # the __init__ method accepts the arguements for general employee information like employee id, full name, and
    # weekly dues to the union services. It initializes the data attributes with these values
    def __init__(self, employee_id, last_name, first_name, weekly_dues):
        self.__employee_id = employee_id
        self.__last_name = last_name
        self.__first_name = first_name
        self.__weekly_dues = weekly_dues

    # Mutator methods for the classes
    # data attributes

    def set_employee_id(self, employee_id):
        self.__employee_id

    def set_full_name(self, last_name, first_name):
        self.__last_name + " " + self.__first_name

    def set_weekly_dues(self, weekly_dues):
        self.__weekly_dues

    # Accessor methods for the classes
    # data attributes

    def get_employee_id(self):
        return self.__employee_id

    def get_full_name(self):
        return self.__last_name + " " + self.__first_name

    def get_weekly_dues(self):
        return self.__weekly_dues


# The Type of Employee represents that of a hourly paid one;
# it is a subclass of the Employee class.
class HourlyEmployee(Employees):
    # the __init__ method accepts the arguments for the general employee information and the
    # specific salaried employee information like employee id, full name, and weekly dues to
    # the union services. It initializes the data attributes with these values

    def __init__(self, employee_id, last_name, first_name, hourly_rate, weekly_dues):
        # Call the superclass's __init__method and pass the arguments necessary for the
        # general employee; self is also passed as an argument.
        Employees.__init__(self, employee_id, last_name, first_name, weekly_dues)

        # inititalizes the __hourly_rate attribute

        self.__hourly_rate = hourly_rate

    # Mutator methods for the __hourly_rate attribute

    def set_salary(self, salary):
        def set_hourly_rate(self, hourly_rate):
            self.__hourly_rate = hourly_rate

    # Accessor methods for the  __hourly_rate attribute

    def get_hourly_rate(self, hourly_rate):
        return self.__hourly_rate


def main():
    # creates an object from the Hourly Employee subclass of the Employee superclass
    # the employee is Adrian Tillman, his pay rate is $25/hour

    adrian = HourlyEmployee("Tillman", "Adrian", "25", "10", "")
    hourly_rate = "his salary is $25/hour"

    # Display the Hourly Employees information

    print(adrian.get_full_name())
    print(hourly_rate.get_hourly_rate())

    # Call the main function


main()