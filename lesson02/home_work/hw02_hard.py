# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
equation = equation.split()
coef = (float(equation[2].strip('x')),float(equation[-1]))
y = coef[0]*x + coef[1]
# вычислите и выведите y


# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

date = '30.02.1985'
date_tuple = tuple(date.split('.'))
day_check_2019 = {'01':'31','02':'30','03':'31','04':'30',
                  '05':'31','06':'30','07':'31','08':'31',
                  '09':'30','10':'31','11':'30','12':'31'}
# test 1. Digits in str
x = 0
for _ in date_tuple:
    if _.isdigit() and len(date_tuple) == 3:
        x += 1
if x == 3:
    print('test 1. Numbers format in input: passed')
    # test 2. Year test
    if len(date_tuple[2])==4:
        print('test 2. year in input: passed')
        x = 1
        # test 3. Month test
        month_max = day_check_2019.get(date_tuple[1],'error')
        if len(date_tuple[1])==2 and month_max!='error':
            print('test 3. month in input: passed')
            # test 4. Day test
            if 1 <= int(date_tuple[0]) <= int(month_max) and len(date_tuple[0])==2:
                print('test 4. day in input: passed')
            else:
                print(('test 4. day in input: failed'))
        else:
            print(('test 3. month in input: failed'))
    else:
        print(('test 2. year in input: failed'))
else:
    print('test 1. Numbers format in input: failed')

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'


# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3
n = int(input('Вход: '))

# disclaimer: длиный, ресурсоемкий, но рабочий способ.

# 1. сгенерируем список размерности вложенных матриц
i_array = list(range(n+1))
i_array.remove(0)
size_array = []
result = [0,0]
j = 0
for i in i_array:
    j = i**2
    size_array.append(j)
       
# 2. сгенерируем словарь с ключами матриц
d = {}
max_val = 0
min_val = 0

for i in size_array:
    max_val = max_val + i
    val_list = list(range(min_val+1,max_val+1))
    min_val = min_val + i
    d[i] = val_list
    

# 3. вычисляем этаж
floor = 0
for key in d.keys():
    if n in d[key]:
        k = d[key]


for key in d.keys():
    if n not in d[key]:
        floor = floor + int(key**0.5)
    else:
        k = d[key]
        dim_k = int(len(k)**0.5)
        if (k.index(n)+1) % dim_k == 0:
            floor = floor + int((k.index(n)+1)/dim_k)
            break
        else:
            floor = floor + int((k.index(n)+1)/dim_k) + 1
            break


# 4. Вычисление горизонтальной позиции квартиры
index_k = []
for i in range(dim_k):
    index_k.extend(list(range(dim_k)))
    
flat_pos = index_k[k.index(n)]+1

# 5. Результаты

result[0] = floor
result[1] = flat_pos
print("Выход: ",result[0],result[1])


#print('квартира №'+str(n)+' расположена на '+str(result[0])+' этаже и на '+str(result[1])+' позиции слева')