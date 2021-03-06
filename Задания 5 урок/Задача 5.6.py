# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
# не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий
# по нему. Вывести словарь на экран.
# Примеры строк файла:
#
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
#
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


def my_split(s):
    for i, c in enumerate(s):
        if not c.isdigit():
            return s[:i]


my_dict = {}
my_list = []
text = str
rez = 0
with open("Test-5.6.txt", "r", encoding="utf_8") as read_obj:
    for line in read_obj:
        text = ''.join(el for el in line if el not in ":().—")
        my_list = text.split()
        f_name = my_list.pop(0)
        for i in my_list:
            rez = rez + int(my_split(i))
        my_dict[f_name] = rez
        rez = 0
    print(my_dict)
