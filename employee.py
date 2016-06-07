class Employees:
    def __init__(self, employee_id, last_name, first_name, weekly_dues):
        self.__employee_id = employee_id
        self.__last_name = last_name
        self.__first_name = first_name
        self.__weekly_dues = weekly_dues

    def get_employee_id(self):
        return self.__employee_id

    def get_full_name(self):
        return self.__last_name + " " + self.__first_name

    def get_weekly_dues(self):
        return self.__weekly_dues


#The Type of Employee represents that of a hourly paid one; 
#it is a subclass of the Employee class. 
class HourlyEmployee(Employees):

    #the __init__ method accepts the arguements for the general employee information and the
    #specific salaried employee information like employee id, full name, and weekly dues to 
    #the union services. It initializes the data attributes with these values
    
    def __init__(self, employee_id, last_name, first_name, hourly_rate, weekly_dues):
        
        #Call the superclass's __init__method and pass the arguements necessary for the 
        #general employee; self is also passed as an arguement.
        Employees.__init__(self, employee_id, last_name, first_name, weekly_dues)
        
        #inititalizes the __hourly_rate attribute
        
        self.__hourly_rate = hourly_rate

      
    #Mutator methods for the __hourly_rate attribute
    
    def set_salary(self, salary):
    def set_hourly_rate(self, hourly_rate):
        self.__hourly_rate = hourly_rate
    
    #Accessor methods for the  __hourly_rate attribute
    
    def get_hourly_rate(self, hourly_rate):
        return self.__hourly_rate

def main():
    adrian = HourlyEmployee("Tillman", "Adrian")
    hourly_rate = "$25/hr"

    print(adrian.get_full_name())
    print(hourly_rate.get_hourly_rate())

