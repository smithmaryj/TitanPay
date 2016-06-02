class Employee:

    def __init__(self):
        self.__last_name = " "
        self.__first_name = " "

    def get_last_name(self):
        return self.__last_name

    def get_first_name(self):
        return self.__first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

if __name__ == "__main__":
    employee_last_name = Employee()
    employee_first_name = Employee()

    employee_last_name.set_last_name("Tillman,")
    employee_first_name.set_first_name("Adrian")
    print("Employee Full Name: " , employee_last_name.get_last_name() , employee_first_name.get_first_name())


