# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
# и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно
# начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def my_func_word(text):
    data = text.title()
    return data


print(my_func_word("word"))


text = str
my_list_up = []
my_list = input("введите строку ").split()
print(my_list)
for i in my_list:
    my_list_up.append(my_func_word(i))
text = " ".join(my_list_up)
print(text)
