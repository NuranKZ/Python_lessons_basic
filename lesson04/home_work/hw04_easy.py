# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

a = [1,2,3,4]

b1 = list(i**2 for i in a) # вариант 1
b2 = list(map(lambda x: x**2, a)) # вариант 2
print(a,b1,b2)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

a = [1,1,2,3,4,1]
b = [4,2,6,8,1]
c = list(set(i for i in a if i in b))
print(c)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

a = [-3,0,3,4, 5, 7, 6, 12]
b = [i for i in a if i%3 == 0 and i>0 and i%4 != 0]
print(b)