# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.


import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp - <file_name> - создание копии файла")
    print("rm - <file_name> - удаление файла")
    print("cd - <file_name> - изменение текущей директории")
    print("ls - отображение полного пути текущей директории")

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

def copy_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.normpath(os.path.join(os.getcwd(),file_name))
    copy_file_name = 'copy_'+file_name
    copy_file_path = os.path.normpath(os.path.join(os.getcwd(),copy_file_name))
    try:
        if os.path.exists(copy_file_path) == True:
            print('копия файла {} уже существует'.format(file_name))
        else:
            shutil.copyfile(file_path,copy_file_path)
            print('файл {} создан'.format(copy_file_name))
    except FileNotFoundError:
        print('файла {} не существует'.format(file_name))

def remove_file():    
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.normpath(os.path.join(os.getcwd(),file_name))
    try:
        os.remove(file_path)
        print('файл {} удален'.format(file_name))
    except FileNotFoundError:
        print('файлa {} не существует'.format(file_name))
    
def change_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.normpath(os.path.abspath(dir_name))
    try:
        os.chdir(dir_path)
        print('текущая директория: ',os.getcwd())
    except Exception:
        print('директории {} не существует'.format(dir_name))    
  
def curr_dir():
    print('текущая директория: ',os.getcwd())
    


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": remove_file,
    "cd": change_dir,
    "ls": curr_dir
}

try:
    dir_name = sys.argv[2]
    file_name = sys.argv[2]
except IndexError:
    dir_name = None
    file_name = None


try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None


try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")