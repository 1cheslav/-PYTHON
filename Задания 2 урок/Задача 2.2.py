#  Для списка реализовать обмен значений соседних элементов, т.е.
#  Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
#  При нечетном количестве элементов последний сохранить на своем месте.
#  Для заполнения списка элементов необходимо использовать функцию input().
my_list = []
print("вводите числа\n", "чтобы закончить ввод чисел - нажмите n" )
while True:
    i = input()
    if i == "n":
        print("вы закончили ввод")
        break
    else:
        my_list.append(int(i))
print("ваши данные", my_list)
if len(my_list)%2 == 0:
    my_list[::2], my_list[1::2] = my_list[1::2], my_list[::2]
else:
    i = my_list.pop()
    my_list[::2], my_list[1::2] = my_list[1::2], my_list[::2]
    my_list.append(i)
print("после сортировки", my_list)
