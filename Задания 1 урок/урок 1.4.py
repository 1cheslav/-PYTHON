#Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
#Для решения используйте цикл while и арифметические операции.

number = list(input('введите целое положительное число '))
print(number)
max_number = 0
i = len(number)-1
while i >= 0:
    if int(number[i]) == 9:
        max_number = int(number[i])
        break
    if int(number[i]) > max_number:
        max_number = int(number[i])
        i -= 1
    else: i -= 1
print(max_number)