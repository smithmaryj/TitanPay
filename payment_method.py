import hourly_employee
import salaried_employee
import Employees
import bank_account

class PaymentMethod(Employees.SalariedEmployee, Employees.HourlyEmployee):
    def __init__(self, mail_payment, pick_up_payment, direct_deposit_payment):
        self.__mail_payment = mail_payment
        self.__pick_up_payment = pick_up_payment
        self.__direct_deposit_payment = direct_deposit_payment


        # Display the payment method information
        print('Mailing a check to Adrian Tillman for $800.00 to 504 College Drive Albany, GA 31705', mail_payment())
        print('A check for $800.00 is waiting for Adrian Tillman at the PostMaster', pick_up_payment())
        print('Direct Deposit information for Adrian Tillman: $800.00')



