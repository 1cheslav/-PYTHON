# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
# числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Data:
    data = input("Введите дату в формате дд-мм-гггг  ").split("-")
    day = month = year = 0

    @classmethod
    def extract_data(cls):
        try:
            Data.day = int(Data.data[0])
            Data.month = int(Data.data[1])
            Data.year = int(Data.data[2])
        except ValueError:
            print("Ошибка, ввода даты")

    @staticmethod
    def valid_data():
        if 31 >= Data.day >= 1:
            print("День - ", Data.day)
        else:
            print("Неправильный день")
        if 12 >= Data.month >= 1:
            print("Месяц - ", Data.month)
        else:
            print("Неправильный месяц")
        if 2100 >= Data.year >= 1900:
            print("Год - ", Data.year)
        else:
            print("Неправильный год")


Data.extract_data()
Data.valid_data()






