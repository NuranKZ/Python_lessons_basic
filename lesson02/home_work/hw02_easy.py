# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

fruit_list = ["яблоко", "банан", "киви", "арбуз"]
x = len(fruit_list)
i = 0
while i<x:
    print('{0}. {1}'.format(i+1,fruit_list[i]))
    i+=1
	
# Подсказка: воспользоваться методом .format()


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
a = [1,2,3,4,5,6]
b = ['a',1,'c']

for item in a:
	for j in b:
		if j == item:
			a.pop(j) 

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
a = [1,3,1,2,4,5,8,9,12]
b = []
for i in a:
	if type(i)!=int:
		print('check inputs')
		break
	else:
		if i%2 == 0:
			b.append(i/4)
		else:
			b.append(i*2)

