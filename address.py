class Address:
    def __init__(self):
        self.__address = " "
        self.__city = " "
        self.__state = " "
        self.__zip = " "

    def get_address(self):
        return self.__address

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zip(self):
        return self.__zip

    def set_address(self, address):
        self.__address = address

    def set_city(self, city):
        self.__city = city

    def set_state(self, state):
            self.__state = state

    def set_zip(self, zip):
            self.__zip = zip

