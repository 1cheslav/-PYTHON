

class Printer(Equipment):
    def __init__(self, model, print_type, name, price, storage, rack, of_branch, date):
        super().__init__(price, name, storage, rack, of_branch, date)
        self.phone_model = model
        self.print_type = print_type


class Scan(Equipment):
    def __init__(self, model, resolution, price, name, storage, rack, of_branch, date):
        super().__init__(price, name,  storage, rack, of_branch, date)
        self.computer_model = model
        self.resolution = resolution


a = Warehouse(10, 123, "A-office", "12.12.2021")
a.in_store()
a.out_store()
