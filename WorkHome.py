# ДЗ №7
#####################################################################
#Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
#под форматами понимаем структуру файлов, например:в файле на одной строке хранится одна
#часть записи, пустая строка - разделитель.

# Вариант №1
# name = input('Введите имя : ')
# surname = input('Введите фамилию: ')
# tel = input('Введите номер телефона: ')
# about = input('Описание: ')

# with open('baz1.py', 'a+', encoding='utf-8') as file:
#   file.write(','.join([name, surname, tel, about]) + '\n')

##############################################################

# Вариат №2

# import csv
# import pandas as pd
# name = input('Введите имя : ')
# surname = input('Введите фамилию: ')
# tel = input('Введите номер телефона: ')
# about = input('Описание: ')


# df = pd.DataFrame(columns =['Name', 'surname', 'tel', 'about'])

# df.loc[1] = [name,surname, tel, about]
# df.to_csv('file,csv')  
#  with open ('baz1.csv','a+',encoding = 'utf-8') as file: 
#   file_writer = csv.writer(file, delimiter  = ',') 
# file_writer.writerow = csv.writer(([name, surname, tel, about]) +'\n') 
      
# print(df)

