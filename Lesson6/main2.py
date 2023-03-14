'''
Дан массив, состоящий из целых чисел. 
Напишите программу, которая в данном массиве определит количество элементов, у которых два соседних и, при этом, 
оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве 
Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

Получение и заполнение массива - в файл1
поиск кол-ва элементов - в файл2

'''
from func import FillArray

array = FillArray()

count = 0
for i in range(1, len(array)-1):
    if array[i-1]<array[i]>array[i+1]:
        count +=1
print(*array)
print(count)

