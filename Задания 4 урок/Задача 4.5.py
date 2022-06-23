# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().


from random import randint
from functools import reduce


def multi(arg_1, arg_2):
    return arg_1 * arg_2


my_list = [randint(100, 1000) for _ in range(25)]
my_list_even = [el for el in my_list if el % 2 == 0]
print(f"Исходный список -  {my_list}\n")
print(f"Чётные числа - {my_list_even}\n")
rez = reduce(multi, my_list_even)
print(f"Результат перемножения - {rez}")



