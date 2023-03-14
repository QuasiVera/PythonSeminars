'''
Задача №17
Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6

'''

spisok = [1, 1, 2, 0, -1, 3, 4, 4, 6, 6]
# list = []
# for i in range(0, len(spisok)):
#     if spisok[i] not in list:
#         list.append(spisok[i])
# print(len(list))

list = set(spisok)
print(len(list))
