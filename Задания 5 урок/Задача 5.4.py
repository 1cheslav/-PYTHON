#  Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


from translate import Translator
with open("test-5.4.txt") as f_obj:
    with open("test-5.4.1.txt", "w", encoding="utf_8") as w_obj:
        for line in f_obj:
            translator = Translator(to_lang='ru')
            rez = translator.translate(line)
            print(rez)
            print(rez, file=w_obj)
