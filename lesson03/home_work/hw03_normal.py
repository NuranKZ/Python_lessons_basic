# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    def inner_fib(x):
        if x == 1 or x == 2:
            return 1
        else:
            return inner_fib(x-2)+inner_fib(x-1)
    fib_list=[]
    if m>n:
        for i in range(m-n+1):
            fib_list.append(inner_fib(n+i))
        return fib_list

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    def find_min(x):
        x_min = None
        for i in x:
            if x_min == None:
                x_min = i
            elif i<=x_min:
                x_min = i
            else:
                x_min = x_min
        return x_min
    
    origin_list_sorted = []
    temp_list = origin_list.copy()
    for i in range(len(origin_list)):
        a = find_min(temp_list)
        origin_list_sorted.append(a)
        temp_list.remove(a)
        
    return origin_list_sorted

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def super_filter(f,S):
    S2 = []
    for i in S:
        if f(i)==True:
            S2.append(i)
    return S2

# check filter func:
def bool_func(x):
    if x>0:
        return True
    else:
        return False

Z = [1,-2,4,0.4,-7]
super_filter(bool_func,Z)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def parr(A1,A2,A3,A4):
    # step1. Внутренняя функция расчета длины стороны
    def len_side(a,b):
        return ( (a[0]-b[0])**2 + (a[1]-b[1])**2 )**0.5
    
    # step2. формируем внутренний словарь со всеми возм.вариантами прямых
    point_set = [A1,A2,A3,A4]
    point_dict = {}
    side_dict = {}
    for idx, i in enumerate(point_set, start=1):
        point_dict[i]=[(i[0]**2+i[1]**2)**0.5]
        k = point_set.index(i)+1
        for j in range(4-idx):
            side = 'point'+str(idx)+'_'+'point'+str(idx+j+1)
            if idx+j+1-idx != 2:
                side_dict[side] = len_side(i, point_set[k])
            k = k+1
    print(side_dict)    
    # step3. формируем множество для проверки
    result_set = set()
    for i in side_dict.values():
        result_set.add(i)
    if len(result_set)==2:
        verdict = 'это Параллелограмм!'
    else:
        verdict = 'это не Параллелограмм!'
    return verdict

# check data:
A1 = (2,1)
A2 = (3,3)
A3 = (6,4)
A4 = (5,2)

parr(A1,A2,A3,A4)