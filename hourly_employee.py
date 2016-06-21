# Mary J Smith, 2295760
# The Employees class represents a superclass of general employee information needed for Titan Payroll to process
import time_card
from employee import Employee 
from time_card import TimeCard

class HourlyEmployee(Employee):
    def __init__(self, hourly_rate):
        self.hourly_rate = hourly_rate

class ListOfTimeCards(time_card.TimeCard):
    # creates a new TimeCard object from the TimeCard class in the
    # time_card.py file
    def __init__(self, clock_in, clock_out, date, time):
        self.clock_in = clock_in
        self.clock_out = clock_out
        self.date = date
        self.time = time
        self.time_card = TimeCard(self, date, time)
        self.__time_card.append(time_card)

    def time_card(self, date, time):
        pass

    def execute(self):
        e = self.get_employee(self.employee_id)
        pc = e.classification
        tc = TimeCard(self.date, self.hours)
        pc.add_time_card(tc)

