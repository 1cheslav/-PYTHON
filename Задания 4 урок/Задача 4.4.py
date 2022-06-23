# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]
# my_list_count = [my_list.count(i) for i in my_list]
# print(my_list_count)


my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_my_list = [el for el in my_list if my_list.count(el) == 1]
print(new_my_list)


new_my_list = []
for i in my_list:
    count = my_list.count(i)
    if count != 1:
        continue
    else:
        new_my_list.append(i)
print(new_my_list)


