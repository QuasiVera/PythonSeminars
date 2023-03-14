'''
39. Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), 
которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива. 
Затем число M - количество элементов во втором массиве. Затем элементы второго массива

'''
from random import randint

array = [ randint(0,10) for i in range (int(input('Введите: ')))]

array2 = [ randint(0,10) for i in range (int(input('Введите: ')))]

print(array)
print(array2)

# for i in array:
#     for j in array2:
#         if i==j:
#             break
#     else:
#         print(i, end = ' ')

for i in array:
        if i not in array2:
            print(i, end = ' ')



