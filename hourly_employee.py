# Mary J Smith, 2295760
# The Employees class represents a superclass of general employee information needed for Titan Payroll to process

import time_card
import Employees

class ListOfTimecards(time_card.TimeCard):
    #creates a new TimeCard object from the Timecard class in the
    #time_card.py file
    def __init__(self, clock_in, clock_out, date, time):
        self.clock_in = clock_in
        self.clock_out = clock_out
        self.date = date
        self.time = time
        timecard = time_card(self, date, time)
        self.__time_card.append(time_card)

def main():
    # creates an object from the Hourly Employee subclass of the Employee superclass
    # the employee is Adrian Tillman, his pay rate is $20/hour

    adrian_HourlyEmployee = Employees.HourlyEmployee('3546255', 'Tillman', 'Adrian', '20', '10')

    # Display the Hourly Employees information

    print('Employee ID:', adrian_HourlyEmployee.get_employee_id())
    print('Last Name:', adrian_HourlyEmployee.get_last_name())
    print('First Name:', adrian_HourlyEmployee.get_first_name())
    print('Weekly Dues:', adrian_HourlyEmployee.get_weekly_dues())


    # Call the main function


main()





