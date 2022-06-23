# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую
# подходящую структуру, например словарь.
# Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.


class Warehouse:
    __product_list = [["xerox", 0], ["printer", 0], ["scaner", 0]]
    storage = "1A"
    rack = 11

    def __init__(self, name, quantity, of_branch=None, shipping_date=None):
        self.quantity = quantity
        self.shipping_date = shipping_date
        self.of_branch = of_branch
        self.name = name

    @staticmethod
    def input_date():
        x = str
        while True:                                         # Ввод общих данных товаров
            x = input("Для выхода из программы ввода введите f или enter чтобы продолжить.")
            if x == "f":
                break
            name = input("Введите тип оборудования - xerox, printer или  scaner -  ")
            quantity = input(" Количество (число) - ")
            direction = input("Движение товара, на склад (in), из склада (out)  - ")
            model = input("Модель - ")
            price = input("Введите стоимость товара (число)  - ")
            if quantity.isdigit():                             # Проверка на корректность (число)
                pass
            elif price.isdigit():
                pass
            else:
                print("Ошибка, введите число.\n")
                continue
            if name == "printer":                           # Ввод данных принтера
                print_type = input("Введите тип печати принтрера (матричный/струйный/лазерный) - ")
                color = input("Цвет печати ч/б или цветной -  ")
                args = [[name, quantity, direction, model, price, print_type, color]]
                Printer.printer_one(args)
            elif name == "xerox":                           # Ввод данных ксерокса
                print_format = input("Формат печати (А0/А3/А4)  - ")
                sys_color = input("Система непрерывной подачи чернил (да/нет) - ")
                args = [name, quantity, model, price, print_format, sys_color]
                Xerox.xerox_one(args)
            elif name == "scaner":
                resolution = input("Максимальное разрешение (число х число dpi) - ")
                scanner_type = input("Тип (планшетный/штрих-код) - ")
                args = [name, quantity, model, price, resolution, scanner_type]
                Scanner.scanner_one(args)
            else:
                print("Неправильный тип оборудования, введите данные снова.\n")

    def in_store(self, *args):                                          # Поступление товара на склад
        for i in range(len(Warehouse.__product_list)):
            if Warehouse.__product_list[i][0] == self.name:
                Warehouse.__product_list[i][1] = Warehouse.__product_list[i][1] + self.quantity
                print(f"{Warehouse.__product_list[i][0]} принят на хранение  - {self.quantity}шт.")
                print("Товара в остатке ", Warehouse.__product_list)

    def out_store(self, quantity):    # Отправка товара со склада
        self.quantity = quantity
        print(f"Отгружаемый товар {self.name}, количество - {self.quantity}шт.")
        for i in range(len(Warehouse.__product_list)):
            if Warehouse.__product_list[i][0] == self.name:
                if Warehouse.__product_list[i][1] < self.quantity:
                    print(f"Количество товара для отгрузки превышает остаток, в наличии - {Warehouse.__product_list[i][1]}шт.")
                    break
                Warehouse.__product_list[i][1] = Warehouse.__product_list[i][1] - self.quantity
                print(f"{Warehouse.__product_list[i][0]} отгружен в подразделение - {self.of_branch}, дата отгрузки - {self.shipping_date}")
                print("Товара в остатке ", Warehouse.__product_list)

    @staticmethod
    def total_counter():                                        # Общий счетчик всех товаров на складе
        __total_counter = 0
        for i in range(len(Warehouse.__product_list)):
            __total_counter = __total_counter + Warehouse.__product_list[i][1]
        print(f"Общее количество товаров на складе - {__total_counter}шт.\n")


class Equipment(Warehouse):
    _printer_list = []
    _xerox_list = []
    _scanner_list = []

    def __equipment_count(self):
        pass


class Printer(Equipment):

    def printer_one(*args):                                     # Формирование списка принтеров
        if args[0][2] == "in":
            a = Warehouse(args)
            Warehouse.in_store(a)




class Xerox(Equipment):
    def xerox_one(*args):                                       # Формирование списка ксероксов
        pass
       # self.quantity = quantity
        #self.name = name


class Scanner(Equipment):                                       # Формирование списка сканеров
    def scanner_one(*args):
        pass
        #self.quantity = quantity
        #self.name = name


a = Xerox("xerox", 10)
a.in_store()
Warehouse.total_counter()

b = Xerox("xerox", 2)
b.in_store()
Warehouse.total_counter()

c = Scanner("scaner", 10)
c.in_store()
Warehouse.total_counter()

d = Printer("printer", 1)
d.in_store()
Warehouse.total_counter()

a.out_store(12)
Warehouse.total_counter()

a.out_store(11)
Warehouse.total_counter()

Warehouse.input_date()
