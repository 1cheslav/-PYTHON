# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени
# сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:

    def __init__(self, name, surname, position):
        wage_data = {"wage": 10000, "bonus": 1500}
        self.name = name
        self.surname = surname
        self.position = position
        self._income = wage_data["wage"] + wage_data["bonus"]


class Position(Worker):

    def get_full_name(self):
        full_name = self.name + " " + self.surname
        return full_name

    def get_total_income(self):
        full_income = self.position + ", полный доход " + str(self._income)
        return full_income


worker = Position("Питер", "Джексон", "инженер")
print(f"{worker.get_full_name()} - {worker.get_total_income()}$")
