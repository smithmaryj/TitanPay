#Mary J Smith, 2295760
#The Employees class represents a superclass of general employee information needed for Titan Payroll to process 

class Employees:
    #the __init__ method accepts the arguements for general employee information like employee id, full name, and 
    #weekly dues to the union services. It initializes the data attributes with these values
    def __init__(self, employee_id, last_name, first_name, weekly_dues):
        self.__employee_id = employee_id
        self.__last_name = last_name
        self.__first_name = first_name
        self.__weekly_dues = weekly_dues
   
    #Mutator methods for the classes 
    #data attributes
    
    def set_employee_id(self, employee_id):
        self.__employee_id

    def set_full_name(self, last_name, first_name):
        self.__last_name + " " + self.__first_name

    def set_weekly_dues(self, weekly_dues):
        self.__weekly_dues
    
    #Accessor methods for the classes 
    #data attributes
    
    def get_employee_id(self):
        return self.__employee_id

    def get_full_name(self):
        return self.__last_name + " " + self.__first_name

    def get_weekly_dues(self):
        return self.__weekly_dues

#The Type of Employee represents that of a salaried one; 
#it is a subclass of the Employee class. 

class SalariedEmployee(Employees):
   
    #the __init__ method accepts the arguements for the general employee information and the
    #specific salaried employee information like employee id, full name, and weekly dues to 
    #the union services. It initializes the data attributes with these values
    
    def __init__(self, employee_id, last_name, first_name, salary, commission_rate, weekly_dues):
        
        #Call the superclass's __init__method and pass the arguements necessary for the 
        #general employee; self is also passed as an arguement.
        Employees.__init__(self, employee_id, last_name, first_name, weekly_dues)
        
        #inititalizes the __salary and __commission_rate attributes
        self.__salary = salary
        self.__commission_rate = commission_rate
    
    #Mutator methods for the __salary and __commission_rate attributes
    def set_salary(self, salary):
        self.__salary = salary

    def set_commission_rate(self, commission_rate):
        self.__commission_rate = commission_rate

    #Accessor methods for the __salary and __commission_rate attributes
    
    def get_salary(self, salary):
        return self.__salary

    def get_commission_rate(self, commission_rate):
        return self.__commission_rate

def main():
    
    #creates an object from the Salaried Employee subclass of the Employee superclass
    #the employee is Mary J Smith, her salary is $65,000/year
    #her commission rate is 10%
    
    maryj = SalariedEmployee("Smith", "Mary J")
    salary = "her salary is $65,000/year"
    commission_rate = "her commission rate is 10%"
    
    #Display the Salaried Employees information
    print (maryj.get_full_name())
    print(salary.get_salary())
    print(commission_rate.get_commission_rate())

#Call the main function
main()


