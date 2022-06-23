# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.


line_count = 0
my_list = []
with open("test-5.2.txt") as f_obj:
    for line in f_obj:
        my_list = line.split(" ")
        line_count += 1
        print(f"Количество слов в строке №{line_count} - {len(my_list)}")
print("Количество строк в файле - ", line_count)

