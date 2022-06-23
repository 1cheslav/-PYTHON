# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(arg1, arg2, arg3):

    my_list = [arg1, arg2, arg3]
    a = 0
    b = 0
    a = my_list.pop(my_list.index(max(my_list)))
    b = my_list.pop(my_list.index(max(my_list)))
    summa = a + b
    return summa


print(my_func(8, 9, 3))
