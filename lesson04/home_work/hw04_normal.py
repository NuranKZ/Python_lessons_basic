# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

# 1.1. Вариант решения без RE
coll = list(line)
res = []

temp_w = ''
for i in coll:
    if i.isupper() == False:
        temp_w+=i
        if coll.index(i) == len(coll)-1:
            res.append(temp_w)
    else:
        if temp_w != '':
            res.append(temp_w)
        temp_w = ''


coll_temp = coll.copy()
coll_temp.reverse()
k = 0
for i in range(len(coll_temp)):
    if coll_temp[i].isupper() != True:
        k = k + 1
    else:
        break

res.append(''.join(coll_temp[0:k])[::-1])
print(res)   


# 1.2. Вариант решения c RE
import re
a = line #"mtMmEZUOmcq"
shablon = r"[a-z]*[a-z]"
res2 = re.findall(shablon,a)
print(res2)

# 1.3. сравнение результатов
print(res == res2)


# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

# 2.1. Вариант решения без RE
coll = list(line)
temp = []
small = ''
big = ''

for i in coll:
    if i.isupper() == True:
        temp.append(small)
        small = ''
        big = big + i
    else:
        temp.append(big)
        big = ''
        small = small + i

temp = [i for i in temp if i!=""]

res = [i[:len(i) - 2] for i in temp if len(i)>=3 and temp[temp.index(i)-1].islower() == True 
       and len(temp[temp.index(i)-1])>1]

print(res)

# 2.2 Вариант решения c RE
shablon = r"[a-z]{2,}([A-Z]{2,})[A-Z]"
res2 = re.findall(shablon,line)
res2 = [i[:-1] for i in res2]
print(res2)

# 2.3 Сверка решений
print(res == res2)


# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

# 3.1 Решение без RE (c записью в файл, вместо random использовал numpy, все равно придется его учить:)

from numpy import random as rnd

inp = list(str(rnd.randint(0,10)) for i in range(2500))

res = [inp[0]]
inp1 = inp[1:]

for idx, i in enumerate(inp1):
    if i == res[-1][-1]:
        res[-1] = res[-1]+i
    else:
        res.append(i)

k = ''
for i in res:
    if len(i)>len(k):
        k = i
           
file = open('result.txt','w')
file.write(k)
file.close()


# 3.2 Решение с RE (без записи в файл, для целей сверки результатов)
str_inp = ''.join(inp)
shablon = r"(0*0)|(1*1)|(2*2)|(3*3)|(4*4)|(5*5)|(6*6)|(7*7)|(8*8)|(9*9)"
res2 = re.findall(shablon,str_inp)

k2 = ''
res3 = []
for i in res2:
    word = ''.join(i)
    if len(word) > len(k2):
        k2 = word

# 3.3 сверка результатов 
print('ответ решения 1: ',k ,'ответ решения 2: ',k2 , 'совпадение: ', k==k2)