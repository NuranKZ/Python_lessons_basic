# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


# РЕШЕНИЕ ОСНОВНОЕ - ОТ ОБЩЕГО к ЧАСТНОМУ
class Univer:
    def __init__(self, univ_name):
        self.univ_name = univ_name
        self.class_list = []

        
class Course:
    def __init__(self):
        #self.teacher_name = teacher_name
        #self.course_name = course_name
        self.course_dict = dict()        
    
    def create_course(self, course_name, teacher_name):
        self.course_dict[course_name]=teacher_name
        return self.course_dict
        
    def show_courses(self):
        for i in self.course_dict.keys():
            print(self.course_dict[i],i)
    
    
class Class(Univer, Course):
    def __init__(self):
        self.class_list = []    
        self.course_dict = dict()
        self.assignation = dict()
        #self.course_list = []
        
    def create_class(self, class_name):
        self.class_list.append(class_name)
        return self.class_list
    
    def show_classes(self):
        for i in self.class_list:
            print(i)
        
    def assign_teacher_class(self,course_name, class_name):
        if ( course_name not in self.course_dict.keys() ) or (
                class_name not in self.class_list):
            print('wrong input')
        else:
            for i in self.class_list:
                if i == class_name:
                    self.key = class_name
                    self.value = self.assignation.get(class_name) or list()
                    self.value.append([course_name,self.course_dict[course_name]])
                    self.assignation[self.key]=self.value
        return self.assignation   
    
    def show_teachers_by_class(self, class_name):
        if class_name not in self.assignation:
            print('wrong input')
        else:
            print('cписок учителей класса ',class_name,':')
            for i in self.assignation.get(class_name):
                print (i[1])
    
    
            
class Student(Class):
    def __init__(self):
        self.student_dict = {}
        self.class_list = []   
        self.assignation = dict()
        self.stud_allocation = dict()
        self.course_dict = dict()
        self.__student_list = []
    
    def add_student(self, student_name, class_name):
        if class_name not in self.class_list:
            print('wrong input')
        else:
            for i in self.class_list:
                if i == class_name:
                    self.key = class_name
                    self.value = self.stud_allocation.get(class_name) or list()
                    self.value.append(student_name)
                    self.stud_allocation[self.key]=self.value            
            self.__student_list.append(student_name)
        return self.stud_allocation
    
    def add_parents(self, student_name, father_name='NA', mother_name='NA'):
        if student_name not in self.__student_list:
            print('wrong input')
        else:
            self.student_dict[student_name] = [father_name, mother_name]
        return self.student_dict

    def show_student_details(self, student_name):
        if student_name not in self.student_dict.keys():
            print('wrong input')
        else:
            print('студент: '+student_name)
            for i,j in self.stud_allocation.items():
                if student_name in j:
                    print('класс: '+i)
                    print('учителя: ')
                    for m in self.assignation[i]:
                        print(m[1])
                    print('предметы: ')
                    for m in self.assignation[i]: 
                        print(m[0])
    
    def show_all_students(self):
        print('список всех учеников школы:')
        for i,j in self.stud_allocation.items():
            for k in j:
                print(k)

    def show_student_parents(self, student_name):
        print(student_name)
        if student_name not in self.__student_list:
            print('wrong input')
        else:
            print('отец: ',self.student_dict[student_name][0])
            print('мать: ',self.student_dict[student_name][1])
        
       
        
# тестирование
# 1. ВВОД данных        
AAA = Student()

AAA.create_class('AI')
AAA.create_class('WEB')
AAA.create_class('GameDev')
#AAA.show_classes()

AAA.create_course('C','Teacher1')
AAA.create_course('Python','Teacher2')
AAA.create_course('DeepLearning','Teacher3')
AAA.create_course('Networks','Teacher4')
#AAA.show_courses()

AAA.assign_teacher_class('Python','AI')
AAA.assign_teacher_class('DeepLearning','AI')
AAA.assign_teacher_class('Python','WEB')
AAA.assign_teacher_class('Networks','WEB')
AAA.assign_teacher_class('C','GameDev')
AAA.assign_teacher_class('Networks','GameDev')
#print(AAA.assignation)

AAA.add_student('Ivanov','AI')
AAA.add_student('Petrov','AI')
AAA.add_student('Sidorova','AI')
AAA.add_student('Melkov','WEB')
AAA.add_student('Krupnova','WEB')
AAA.add_student('John Snow','GameDev')
AAA.add_student('D. Targaryen','GameDev')
#print(AAA.stud_allocation)

AAA.add_parents('Ivanov','Ivanych','Ivanova')
AAA.add_parents('Petrov','Petrovich','Petrova')
AAA.add_parents('John Snow','Bastard','Petrova')
AAA.add_parents('D. Targaryen','Crazy King','I dont remember')
#print(AAA.student_dict)

# 1. Получить полный список всех классов школы 
AAA.show_classes()

# 2. Получить полный список всех учеников школы 
AAA.show_all_students()

# 3. Получить список всех учеников в указанном классе
AAA.show_student_details('John Snow')

# 4. Узнать ФИО родителей указанного ученика
AAA.show_student_parents('D. Targaryen')

# 5. Получить список всех Учителей, преподающих в указанном классе
AAA.show_teachers_by_class('AI')


# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе







# 2й ВАРИАНТ РЕШЕНИЯ - хуже чем первый - ОБРАТНАЯ ИЕРАРХИЯ от Ученика к Школе
'''
class Parents:
    def __init__(self, father, mother):
        self.father = father
        self.mother = mother
    
    def show_info(self):
        self.message = ('Папа - '+self.father )
        self.message += ('\nМама - '+self.mother)
        return self.message 

class Student(Parents):
    def __init__(self, student_name, father = 'not filled', 
                 mother = 'not filled'):
        self.student_name = student_name
        #self.father = father
        #self.mother = mother
    
    def show_info(self):
        self.message = super(Student, self).show_info()
        self.message = ('student\'s name - '+self.student_name 
                        +'\n'+self.message)
        return self.message
    

class Group(Student):
    def __init__(self, group_name):
        self.group_name = group_name
        self.student_list = []
        self.course_dict = dict()

        
    def add_course(self, course_name, teacher_name):
        self.course_dict[course_name] = teacher_name
        print(teacher_name+' теперь преподает '+course_name+' в '+
              self.group_name+' классе')
        return self.course_dict        

        
    def del_course(self, teacher_name):
        try:
            del self.course_dict[teacher_name]
            print(teacher_name + ' уже не работает с этим классом')
        except Exception:
            print(teacher_name+' итак не преподает здесь')
        finally:
            return self.course_dict
        
    def add_student(self, student_name, father, mother):
        self.student_list.append([student_name, father, mother])
        print(student_name + ' поступил в класс '+self.group_name)
        return self.student_list
        
    def del_student(self, student_name):
        try:
            self.student_list.remove(student_name)
            print(student_name + ' исключен из класса')
        except Exception:
            print(student_name+' не учился в этом классе')
        finally:
            return self.student_list

    def show_student_info(self, student_name):
        try:    
            self.student_name = student_name
            for i in self.student_list:
                if i[0]==student_name:
                    self.father = i[1]
                    self.mother = i[2]
            self.message = super(Group, self).show_info()
            self.message = (self.message+'\nУчится в группе '+
                            self.group_name)
            print(self.message)
        except Exception:
            print('Такого у нас нету')
    def show_all_students(self):
        print('список учеников класса '+self.group_name)
        for idx, i in enumerate(self.student_list):
            print(str(idx+1)+'. '+ i[0])
    
    def show_student_courses(self, student_name=''):
        __studlist = list(i[0] for i in self.student_list)
        if student_name not in __studlist:
            print('такой у нас не учится')
        else:
            print('студент '+student_name+' учиться в классе '
                      +self.group_name )
            print('изучаемые предметы: ')
            for j in self.course_dict.keys():
                print(self.course_dict[j] + ' : '+j)
    
    def show_teachers(self):
        print('в классе '+self.group_name+' следующие предметы: ')
        for i in self.course_dict.keys():
            print(self.course_dict[i]+" : "+i)



class School():
    def __init__(self):
        self.group_list = []
    
    def add_group(self, group_name):
        self.group_list.append(group_name)
        return self.group_list

    def del_group(self, group_name):
        self.group_list.remove(group_name)
        return self.group_list
    
    def show_groups(self):
        for i in self.group_list:
            print(i.group_name)
        

#Ввод условных данных

testlist1 = [['Иванов И.И.','Иванов И.Ф','Иванова А.А.'],
            ['Петров П.В.','Петров В.В.','Непетрова Н.Р.'],
            ['Леннон Д.Л.','Black J.J.','Unknown'],
            ['Есенина Е.Г.','Есенин Г.Г.','Есенина М.М.'],
            ['Леопольд П.Т.','Леопольд Т.Л.','Леопольд М.М.']]

testlist2 = [['Таргариен Д.Б.','Таргариен Б.К.','Таргариен С.С.'],
            ['Сноу Д.Б.','Старк','Неизвестно'],
            ['R2D2','Undefined','Undefined']]

GB = School()
G1 = Group('11A')
G2 = Group('7B')
for i in testlist1:
    G1.add_student(i[0],i[1],i[2])

for i in testlist2:
    G2.add_student(i[0],i[1],i[2])
    
G1.add_course('Python','Россум Г.')
G2.add_course('Python','Россум Г.')
G1.add_course('История Научного Коммунизма','Ленин В.И.')
G2.add_course('Литература','Пушкин А.С.')

GB.add_group(G1)
GB.add_group(G2)

# Тестирование функций
#1. Полный список всех классов школы
GB.show_groups()

#2. Список учеников класса
G1.show_all_students()
G2.show_all_students()

#3. Список изучаемых предметов студента

#G1.show_student_courses('R2D2')
G2.show_student_courses('R2D2')

#4. Список преподавателей класса
G1.show_teachers()
G2.show_teachers()

#5. Детальная информация о студенте
#G2.show_student_info('Сноу Д.Б.')
G1.show_student_info('Иванов И.И.')

'''