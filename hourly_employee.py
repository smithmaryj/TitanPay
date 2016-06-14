# Mary J Smith, 2295760
# The Employees class represents a superclass of general employee information needed for Titan Payroll to process

import Employees

def main():
    # creates an object from the Hourly Employee subclass of the Employee superclass
    # the employee is Adrian Tillman, his pay rate is $25/hour

    adrian_HourlyEmployee = Employees.HourlyEmployee('0246857', 'Tillman', 'Adrian', '25', '10')

    # Display the Hourly Employees information

    print('Employee ID:', adrian_HourlyEmployee.get_employee_id())
    print('Last Name:', adrian_HourlyEmployee.get_last_name())
    print('First Name:', adrian_HourlyEmployee.get_first_name())
    print('Weekly Dues:', adrian_HourlyEmployee.get_weekly_dues())


    # Call the main function


main()
        

    
    
   
