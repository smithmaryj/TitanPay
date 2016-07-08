import csv
from accounting.employee import Employee

csv.register_dialect(
    print('\n Hourly Employee Information'),

    'mydialect'
with open('hourly_employees.csv', 'r') as mycsvfile:
    dictofdata = csv.DictReader(mycsvfile, dialect='mydialect')
    for row in dictofdata:
        print(row['EmployeeId'] + "\n " + row['LastName'] + "\n " + row['FirstName']
              + "\n " + row['HourlyRate'] + "\n " + row['UnionDues'] + '\n ' + row['PaymentMethod'])

class Employees_dict():

    def __init__(self, id, last, first, dues, pay):
        self.employee_id = id
        self.last_name = last
        self.first_name = first
        self.weekly_dues = dues
        self.payment_method = pay

    def displayEmployee(self):
        print("Employee Id : ", self.employee_id)
        print("Last Name : ", self.last_name)
        print("First Name : ", self.first_name)
        print("UnionDues : ", self.weekly_dues)
        print("PaymentMethod : ", self.payment_method)
        print()
