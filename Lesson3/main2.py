'''
Задача №19
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [3, 4, 5, 1, 2]
'''
spisok = [1, 2, 3, 4, 5, 6, 7]
k = int(input('Введите число сдвига: '))
temp = None
for i in range(0, k):
    for j in range(len(spisok)-1, 0, -1):
        temp = spisok[j]
        spisok[j] = spisok[j-1]
        spisok[j-1]= temp
print(spisok)