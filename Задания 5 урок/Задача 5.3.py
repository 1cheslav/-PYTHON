# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


m_salary = count = 0
my_dict = {}
with open("test-5.3.txt") as f_obj:
    print("Исходные данные ")
    for line in f_obj:
        print(line)
        data = line.split(" ")
        my_dict[data[0]] = data[1].strip("\n")
print("Сотрудники с зарплатой менее 20000")
for i in my_dict:
    m_salary = m_salary + int(my_dict[i])
    count += 1
    if int(my_dict[i]) < 20000:
        print(i)
print("Средняя величина дохода ", m_salary/count)
