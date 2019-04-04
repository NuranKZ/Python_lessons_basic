# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import sys
import shutil

def generate_folder(x):
    #global folder
    os.mkdir(x)
    print(x, ' folder was created')
    
def delete_folder(x):    
    #global folder
    os.rmdir(x)
    print(x, ' folder was deletted')

def show_content():
    #print('here are all elements in chosen folder:')
    for _ in os.listdir('.'):
        print(_)


    
# код ниже был закомментирован для отключения исполнения при
# импорте файла как модуля в задачу normal
# для проверки задач easy - раскомментируйте код ниже
    
folder_names = ['dir_'+ str(i) for i in range(1,10)]

'''
for folder in folder_names:
	try:
		generate_folder(folder)
	except FileExistsError:
		print(folder,' is exist')
		continue


for folder in folder_names:
	try:
		delete_folder(folder)
	except FileNotFoundError:
		print(folder,' isn\'t exist')
		continue

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
show_content()


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


#os.getcwd
current_file_path = sys.argv[0]
current_file = os.path.basename(current_file_path)
new_file = "copy_"+current_file
new_file_path = os.path.join(os.path.dirname(current_file_path),new_file)

if os.path.exists(new_file_path) == True:
    print('Copy already exist')
else:
    shutil.copyfile(current_file_path, new_file_path)
'''

