'''
В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. 
За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. 
Выведите наименьшее число парт, которое нужно приобрести для них. Без циклов и if'ов и без функций

**Input:**

20 

21 

22

**Output:**

32

'''

# c1 = int(input('Число учеников класса 1: '))
# c2 = int(input('Число учеников класса 2: '))
# c3 = int(input('Число учеников класса 3: '))
# n = (c1+1)//2 + (c2+1)//2 + (c3+1)//2
# print(f'миниальное количество парт равно {n}')
'''
Дано натуральное число. 
Дано натуральное число. Требуется определить, является ли год с данным номером високосным.
 Если год является високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии с григорианским календарем, 
год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.

**Input:**

2016

**Output:**

YES
'''
y = int(input('Введите год: '))
visokos = y%400 ==0 or y%4==0 and y%100!=0
if visokos:
    print('Yes')
else:
    print("No")