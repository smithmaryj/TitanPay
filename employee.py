from accounting.address import Address

class Employee:

    def __init__(self, id, last, first, dues, pay, street_address, city, state, zip):
        self.employee_id = id
        self.last_name = last
        self.first_name = first
        self.weekly_dues = dues
        self.payment_method = pay
        self.street_address = Address(street_address, city, state, zip)
        self.full_address = street_address + ", " + city + ", " + state + " " + zip

    def get_full_name (self):
        full_name = self.__last_name + " " + self.__first_name
        return full_name

    def get_dues (self):
        return self.__weekly_dues

    def get_pay (self):
        return self.__payment_method

    def get_full_address (self):
        return self.__full_address
