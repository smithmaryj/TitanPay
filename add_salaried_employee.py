from employee import Employee

from add_employee import AddEmployee


class AddSalariedEmployee(AddEmployee):
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def execute(self):
        self.e = Employee(self.name, self.address)
        self.make_classification()

        return self.e.id
