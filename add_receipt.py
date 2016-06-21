from receipt import Receipt

class AddReceipt(object):
    def __init__(self, employee_id, date, amount):
        self.employee_id = employee_id
        self.date = date
        self.amount = amount

    def execute(self):
        e = self.get_employee(self.employee_id)
        pc = e.classification
        pc.add_receipt(Receipt(self.date, self.amount))