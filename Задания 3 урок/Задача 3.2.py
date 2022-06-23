# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def humen_data (name, second_name, year, city, email, phone):
    print(f"имя - {name}, фамилия - {second_name}, год рождения - {year}, город - {city}, почта - {email}, № телефона - {phone}")


name = input("введите имя ")
second_name = input("введите фамилию ")
year = input("введите год рождения ")
city = input("введите город проживания ")
email = input("введите email ")
phone = input("введите номер телефона ")
humen_data(name, second_name, year, city, email, phone)
