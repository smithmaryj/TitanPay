class SalariedEmployee:

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
    salariedemployee_last_name = SalariedEmployee()
    salariedemployee_first_name = SalariedEmployee()

    salariedemployee_last_name.set_last_name("Tillman,")
    salariedemployee_first_name.set_first_name("Adrian")
    print("Salaried Employee Full Name: " , salariedemployee_last_name.get_last_name() , salariedemployee_first_name.get_first_name())


