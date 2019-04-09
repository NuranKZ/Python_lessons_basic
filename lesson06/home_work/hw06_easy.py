# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
class Triangle:
    def __init__(self, a=(0,0), b=(0,0), c=(0,0)):
        self.a = a
        self.b = b
        self.c = c
        
    def perimeter(self):
        self.__ab = ((self.b[0]-self.a[0])**2 + (self.b[1]-self.a[1])**2)**0.5
        self.__ac = ((self.c[0]-self.a[0])**2 + (self.c[1]-self.a[1])**2)**0.5
        self.__bc = ((self.c[0]-self.b[0])**2 + (self.c[1]-self.b[1])**2)**0.5
        self.__len_list = [self.__ab, self.__ac, self.__bc]
        return self.__ab + self.__ac + self.__bc

    def square(self):
        self.s = sum(self.__len_list)/2
        self.sq = (self.s*(self.s - self.__ab)*(self.s - self.__ac)
                    *(self.s - self.__bc))**0.5
        if self.sq == 0:
            print('It is line!')
        else:
            return self.sq

    def height(self):
        try:
            if self.sq == 0:
                print('not applicable to line')
            else:
                self.height = [(2*self.sq)/self.__ab, (2*self.sq)/self.__ac,
                               (2*self.sq)/self.__bc]
                return self.height
        except ZeroDivisionError:
            print('wrong coordinates')
        

# Проверка
ex1 = Triangle([0,0],[0,1],[1,0])
#print(ex1.perimeter())
#print(ex1.square())
#print(ex1.height())

ex2 = Triangle([0,0],[0,0],[1,1])
#print(ex2.perimeter())
#print(ex2.square())
#print(ex2.height())

     
ex3 = Triangle([1,2],[3,4],[5,6])
#print(ex3.perimeter())
#print(ex3.square())
#print(ex3.height())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


# ПРИМЕЧАНИЕ: ЗДЕСЬ УПРОЩЕННОЕ РЕШЕНИЕ В ТОМ СМЫСЛЕ,
# ЧТО КООРДИНАТЫ НАДО ВВОДИТЬ ПО ТОЧКАМ, РЕАЛЬНО СЛЕДУЮЩИМ ДРУГ ЗА ДРУГОМ

class Trapezium:
    def __init__(self, a=(0,0), b=(0,0), c=(0,0), d= (0,0)):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.__ab = 0
        self.__bc = 0
        self.__cd = 0
        self.__da = 0
        self.__figure = []
        
    
    def perimeter(self):
        self.__ab = ((self.b[0]-self.a[0])**2 + (self.b[1]-self.a[1])**2)**0.5
        self.__bc = ((self.c[0]-self.b[0])**2 + (self.c[1]-self.b[1])**2)**0.5
        self.__cd = ((self.d[0]-self.c[0])**2 + (self.d[1]-self.c[1])**2)**0.5
        self.__da = ((self.a[0]-self.d[0])**2 + (self.a[1]-self.d[1])**2)**0.5
        return self.__ab + self.__bc + self.__cd + self.__da

    def check(self):
        self.perimeter()
        self.__figure = [self.__ab, self.__bc, self.__cd, self.__da]
        self.__figangles = 4 - self.__figure.count(0)
        
        if self.__figangles == 4:
            if len(set(self.__figure)) == 2:
                print('Parallelogram, wrong coordinates')
            elif len(set(self.__figure)) == 4:
                print('It is not trapezium, wrong coordinates')
            elif self.__ab != self.__cd:
                print('It is not trapezium, wrong coordinates')
            else:    
                print('test is ok, it is Trapezium')
        else:
            print('it is not quadrilateral')
    def square(self):
        self.__sq = ((self.__da+self.__bc)/2)*(self.__ab**2 
                    - 0.25*(self.__da-self.__bc)**2)**0.5
        return self.__sq

    def height(self):
        self.__height = (self.__ab**2 - 
                         0.25*(self.__da-self.__bc)**2)**0.5
        return self.__height
    
# Проверка    

ex4 = Trapezium([0,0],[0,0],[1,1],[0,1])
ex4.check()
print(ex4.perimeter())
print(ex4.square())
print(ex4.height())

ex5 = Trapezium([0,0],[1,3],[4,3],[5,0])
ex5.check()
print(ex5.perimeter())
print(ex5.square())
print(ex5.height())

ex6 = Trapezium([0,0],[1,3],[4,3],[3,0])
ex6.check()
print(ex6.perimeter())
print(ex6.square())
print(ex6.height())




