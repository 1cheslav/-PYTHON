# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

try:
    with open("test-5.1.txt", "w") as f_obj:
        while True:
            user_data = input("Введите данные ")
            if not user_data:
                break
            f_obj.writelines(user_data)
except IOError:
    print("Ошибка ввода")




