import Employees

class Receipt(Employees.SalariedEmployee):

    def __init__(self, receipt_date, sale_amount):
                self.receipt_date = receipt_date
                self.sale_amount = sale_amount

