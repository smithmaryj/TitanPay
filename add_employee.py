import employee
import add_employee
import salaried_employee
import hourly_employee

class AddEmployee(object):
    def __init__(self, name, address):
        self.name = name
        self.address = address


    def execute(self):
        self.e = employee.Employee(self.name, self.address)
        self.make_classification()

        return self.e.id

class AddHourlyEmployee(add_employee.AddEmployee):
    def __init__(self, name, address, hourly_rate):
        add_employee.AddEmployee.__init__(self, name, address)
        self.hourly_rate = hourly_rate

    def make_classification(self):
        self.e.classification = hourly_employee.HourlyEmployee(self.hourly_rate)



class AddSalariedEmployee(AddEmployee):
    def __init__(self, name, address, salary, db):
        add_employee.AddEmployee.__init__(self, name, address, db)
        self.salary = salary

    def make_classification(self):
        self.e.classification = salaried_employee.SalariedEmployee(self.salary)

