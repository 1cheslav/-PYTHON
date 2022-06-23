# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.


import time


class TrafficLight:

    def __init__(self, color1, color2, color3, cycle_count=3, color1_time=5, color2_time=2, color3_time=5):
        self.__color1_time = color1_time
        self.__color2_time = color2_time
        self.__color3_time = color3_time
        self.__color1 = color1
        self.__color2 = color2
        self.__color3 = color3
        self.cycle_count = cycle_count

    def running(self):
        a = 0
        print("по умолчанию программа остановится после трех циклов работы светофора.")
        while True:
            if a == self.cycle_count:
                print("Программа остановлена")
                break
            if self.__color1 == "красный":
                print("красный")
                time.sleep(self.__color1_time)
            else:
                print("цвет не правильный!")
                break
            if self.__color2 == "желтый":
                print("желтый")
                time.sleep(self.__color2_time)
            else:
                print("цвет не правильный!")
                break
            if self.__color3 == "зеленый":
                print("зеленый")
                time.sleep(self.__color3_time)
            else:
                print("цвет не правильный!")
                break
            a += 1


a = TrafficLight("красный", "желтый", "зеленый", 3)
a.running()
