# Mary J Smith, 2295760
# The Employees class represents a superclass of general employee information needed for Titan Payroll to process

import Employees
import receipt

class CommissionRate (Employees.SalariedEmployee):
    def __init__(self, sale_amount):
        receipt.__init__(self, sale_amount)



class ListOfReceipts(receipt.Receipt):
    def __init__(self, receipts):
        self.__receipts = []
        receipts = receipts(self, '12-14-2016', '1-13-16', '2-13-16', '3-16-16')

def main():
    # creates an object from the Salaried Employee subclass of the Employee superclass
    # the employee is Mary J Smith, her salary is $65,000/year
    # her commission rate is 10%

    maryj_SalariedEmployee = Employees.SalariedEmployee('2295760', 'Smith', 'Mary J', '25' '65000', '10')

    # Display the Salaried Employees information

    print('Employee ID:', maryj_SalariedEmployee.get_employee_id())
    print('Last Name:', maryj_SalariedEmployee.get_last_name())
    print('First Name:', maryj_SalariedEmployee.get_first_name())
    print('Weekly Dues:', maryj_SalariedEmployee.get_weekly_dues())
    print('Her salary is:', maryj_SalariedEmployee.get_salary())
    print('Her commission rate is:', maryj_SalariedEmployee.get_commission_rate())

# Call the main function
main()

#this has no error but doesn't print...grrr!!!







