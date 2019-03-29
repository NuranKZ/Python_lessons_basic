# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

input1 = input('введите выражение, не забудьте пробелы между числами и знаком: ')
#input1 = '3/2 + 10/3'

#1 step. Reformatting (parse)
data = list(input1.split(' '))
data2 = []
for i in (0,2):
    number = data[i].split('/')
    number2 = []
    for j in number:
        number2.append(int(j))
        
    data2.append(number2)

for i in data2:
    if len(i)==1:
        i.append(1) 
    
if data[1]=='-':
    data2[1][0] = data2[1][0]*(-1)
    

#2 Calculating prelim result
prelim_res = []
if data2[0][1]==0 or data2[1][1]==0:
    stop = 1
else:
    stop = 0
    denominator = data2[0][1]*data2[1][1]
    nominator = data2[0][0]*data2[1][1] + data2[0][1]*data2[1][0]
    prelim_res = [nominator, denominator]
    

#3 Modifying result
if abs(denominator) < abs(nominator):
    a1 = nominator//denominator
    a2 = nominator - denominator*a1
    a3 = denominator
else:
    for x in range(2,nominator+1):
        if nominator%x == 0 and denominator%x == 0:
            nominator = int(nominator/x)
            denominator = int(denominator/x)
    a1 = ''
    a2 = nominator
    a3 = denominator

if a2 == 0:
    a2 = ''
    a3 = ''

#4 Print output
if stop == 1:
    print('input error!: div/0')
else:
    if a2 == a3 and a2 != '':
        print(int(int(a2)/int(a3)))
    elif a2 == '':
        print(a1)
    else:
        print(a1, str(a2)+'/'+str(a3))

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
