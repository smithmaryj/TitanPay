class Address:

    def __init__(self):
        self.__street_address = " "
        self.__city = " "
        self.__state = " "
        self.__zip = " "

    def get_street_address(self):
        return self.__street_address

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zip(self):
        return self.__zip

    def set_street_address(self, street_address):
        self.__street_address = street_address

    def set_city(self, city):
        self.__city = city

    def set_state(self, state):
            self.__state = state

    def set_zip(self, zip):
            self.__zip = zip


if __name__ == "__main__":
    address_street_address = Address()
    address_city = Address()
    address_state = Address()
    address_zip = Address()

    address_street_address.set_street_address("6006 5th Ave. N.")
    address_city.set_city("St. Petersburg,")
    address_state.set_state("Fl.")
    address_zip.set_zip("33712")
    print("Address: " , address_street_address.get_street_address() , address_city.get_city() , address_state.get_state() , address_zip.get_zip())




