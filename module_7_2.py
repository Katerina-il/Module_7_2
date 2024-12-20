import io
from pprint import pprint

"""
Домашнее задание по теме "Позиционирование в файле"
Цель: Закрепить знания о позиционировании в файле, использовав метод tell() файлового объекта. 
Написать усовершенствованную функцию записи.
Задача "Записать и запомнить":
Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла для записи, 
strings - список строк для записи.
Функция должна:
Записывать в файл file_name все строки из списка strings, каждая на новой строке.
Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>), 
а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.
Пример полученного словаря:

"""

def custom_write(file_name, strings):

    strings_positions = {}
    key_string = 0
     #Записывать в файл file_name все строки из списка strings, каждая на новой строке
    for string in strings:
        file_name_open = open (file_name, 'a', encoding ='utf-8')
        key_tuple_1 = file_name_open.tell()
        key_string += 1
        strings_positions [key_string, key_tuple_1] = string
        file_name_open.writelines(string + '\n')
        file_name_open.tell()
        #file_name_open_abc.tell ()
        file_name_open.close()
    return strings_positions




info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]



result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)