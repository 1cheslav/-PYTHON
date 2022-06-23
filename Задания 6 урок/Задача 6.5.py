# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    title = "название"

    def __init__(self):
        pass

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def draw(self):
        print("Ручка рисует")


class Pencil(Stationery):

    def draw(self):
        print("Карандаш рисует")


class Handle(Stationery):

    def draw(self):
        print("Маркер рисует")


s = Stationery()
s.draw()
print(s.title)
p = Pen()
p.draw()
ps = Pencil()
ps.draw()
h = Handle()
h.draw()


