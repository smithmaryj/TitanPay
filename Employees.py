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

    def set_last_name(self, last_name):
        self.__last_name

    def set_first_name(self, first_name):
        self.__first_name

    def set_weekly_dues(self, weekly_dues):
        self.__weekly_dues

    # Accessor methods for the classes
    # data attributes

    def get_employee_id(self):
        return self.__employee_id

    def get_last_name(self):
        return self.__last_name

    def get_first_name(self):
        return self.__first_name

    def get_weekly_dues(self):
        return self.__weekly_dues


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

        def set_hourly_rate(self, hourly_rate):
            self.__hourly_rate = hourly_rate

    # Accessor methods for the  __hourly_rate attribute

    def get_hourly_rate(self, hourly_rate):
        return self.__hourly_rate


# The Type of Employee represents that of a salaried one;
# it is a subclass of the Employee class.

class SalariedEmployee(Employees):
    # the __init__ method accepts the arguments for the general employee information and the
    # specific salaried employee information like employee id, full name, and weekly dues to
    # the union services. It initializes the data attributes with these values

    def __init__(self, employee_id, last_name, first_name, salary, commission_rate, weekly_dues):
        # Call the superclass's __init__method and pass the arguments necessary for the
        # general employee; self is also passed as an argument.
        Employees.__init__(self, employee_id, last_name, first_name, weekly_dues)

        # inititalizes the __salary and __commission_rate attributes
        self.__salary = salary
        self.__commission_rate = commission_rate

    # Mutator methods for the __salary and __commission_rate attributes
    def set_salary(self, salary):
        self.__salary = salary

    def set_commission_rate(self, commission_rate):
        self.__commission_rate = commission_rate

    # Accessor methods for the __salary and __commission_rate attributes

    def get_salary(self, salary):
        return self.__salary

    def get_commission_rate(self, commission_rate):
        return self.__commission_rate
