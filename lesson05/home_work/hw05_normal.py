# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

# test of importing

import hw05_easy as easy
import os
import sys
#import shutil

#victim = 'f2'
#easy.delete_folder(victim)
def goto_folder(x):
    #global folder
    os.chdir(x)
    print(os.getcwd())

# main code

options = {
        '1. Перейти в папку': goto_folder,
           '2. Посмотреть содержимое папки': easy.show_content,
           '3. Удалить папку': easy.delete_folder,
           '4. Создать папку': easy.generate_folder
           }

print('Наше Меню на сегодня:')
for key in options.keys():
    print(key)
print('****Для выхода из программы введите пустой или неправильный ключ****')

try:
    user_input = sys.argv[1]
except IndexError:
    print('ключ не введен,\nвыход из программы')
else: 
    while True:
        try:
            user_input
        except IndexError:
            print('ключ не введен,\nвыход из программы')
            sys.exit()
        else:
            if user_input == '1':
                try:
                    print('переход в папку')
                    folder = input('введите имя папки: ')
                    options['1. Перейти в папку'](folder)
                except FileNotFoundError:
                    print('Невозможно перейти')
                else:
                    print('перешел в ', folder)                 
            elif user_input == '2':
                print('содержание текущей директории:')
                options['2. Посмотреть содержимое папки']()        
            elif user_input == '3':     
                try:
                    print('удаление папки в текущей директории')
                    folder = input('введите имя папки: ')
                    options['3. Удалить папку'](folder)
                except FileNotFoundError:
                    print('Невозможно удалить')
                else:
                    print(folder, 'успешно удалена')            
            elif user_input == '4':
                try:
                    print('создание папки в текущей директории')
                    folder = input('введите имя папки: ')
                    options['4. Создать папку'](folder)
                except FileExistsError:
                    print('Невозможно создать')    
                else:
                    print(folder, 'успешно создана')  
            else:
                print('введено неверное значение ключа\n выход из программы')
                sys.exit()
            
            user_input = input('введите команду еще раз: ')








