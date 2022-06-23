# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Автомобиль поехал")

    def stop(self):
        print("Автомобиль остановился")

    def direction(self):
        print("Повернул налево")

    def show_speed(self):
        if self.speed > 100:
            print(f"Превышение скорости на {self.speed - 100} км/ч\n")
        else:
            print(f"скорость {self.speed} км/ч\n")


class TownCar(Car):

    def townCar(self):
        print(f"Городской автомобиль {self.name} {self.color}")
        if self.is_police:
            print("Имеет преимущество на дороге")
        else:
            print("Нет преимущества на дороге")

    def show_speed(self):
        if self.speed > 60:
            print(f"Превышение скорости на {self.speed - 60} км/ч\n")
        else:
            print(f"скорость {self.speed} км/ч\n")


class SportCar(Car):

    def sportCar(self):
        print(f"Спортивный автомобиль {self.name} {self.color}")
        print("Потенциальный нарушитель")
        if self.is_police:
            print("Имеет преимущество на дороге")
        else:
            print("Нет преимущества на дороге")


class WorkCar(Car):

    def workCar(self):
        print(f"Рабочий автомобиль {self.name} {self.color}")
        if self.is_police:
            print("Имеет преимущество на дороге")
        else:
            print("Нет преимущества на дороге")

    def show_speed(self):
        if self.speed > 40:
            print(f"Превышение скорости на {self.speed - 40} км/ч\n")
        else:
            print(f"скорость {self.speed} км/ч\n")


class PoliceCar(Car):

    def policeCar(self):
        print(f"Автомобиль полиции {self.name} {self.color}")
        if self.is_police:
            print("Имеет преимущество на дороге")
        else:
            print("Нет преимущества на дороге")


car_1 = TownCar(65, "белый", "Жигули", False)
car_1.townCar()
car_1.stop()
car_1.go()
car_1.show_speed()

car_2 = SportCar(199, "красный", "Феррари", False)
car_2.sportCar()
car_2.go()
car_2.direction()
car_2.show_speed()

car_3 = WorkCar(40, "грязный", "Катерпиллер", False)
car_3.workCar()
car_3.stop()
car_3.go()
car_3.show_speed()

car_4 = PoliceCar(60, "с мигалками", "Москвич", True)
car_4.policeCar()
car_4.go()
car_4.direction()
car_4.show_speed()
