'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.

11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12

'''

from random import randint
number1 = int(input('Введите число элементов списка 1: '))
number2 = int(input('Введите число элементов списка 2: '))

plenty1 = []
plenty2 = []

for i in range(number1):
    plenty1.append(randint(0,10))

for i in range(number2):
    plenty2.append(randint(0,10))

result = sorted(list(set(plenty1)&set(plenty2)))

print(plenty1, plenty2)
print(result)