class Account:

    def __init__(self):
        self.__bank_name = " "
        self.__routing_number = " "
        self.__account_id = " "
        self.__deposit_amt = " "

    def get_bank_name(self):
        return self.__bank_name

    def get_routing_number(self):
        return self.__routing_number

    def get_account_id(self):
        return self.__account_id

    def get_deposit_amt(self):
        return self.__deposit_amt

    def set_bank_name(self, bank_name):
        self.__bank_name = bank_name

    def set_routing_number(self, routing_number):
        self.__routing_number = routing_number

    def set_account_id(self, account_id):
        self.__account_id = account_id

    def set_deposit_amt(self, deposit_amt):
        self.__deposit_amt = deposit_amt

