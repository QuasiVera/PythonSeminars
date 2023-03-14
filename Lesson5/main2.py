'''
Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

'''
array = [int(i) for i in input().split()]


def ChangeMaxtoMin(array):
    min = max = array[0]
    
    for i in array:
        if i > max:
            max = i
        if i < min:
            min = i
    for i in range(len(array)):
        if array[i] == max:
            array[i] = min
    return array


print(ChangeMaxtoMin(array))
