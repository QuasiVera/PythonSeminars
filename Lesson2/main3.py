
n = int(input('Введите число дней: '))
i = 0
count = 0

max = 0
while i<n:
    t = int(input('Введите температуру: '))
    if t>0:
        count+=1
    else:
        if count > max:
            max = count
            count = 0
    i +=1
if count > max:
        max = count
print(max)



# n - число арбузов
# найти минимум и максимум веса

n = int(input())
max = 0
min = 10000000 #
for i in range(n):
    ves_arbyz = int(input())
    if ves_arbyz < min:
        min = ves_arbyz
    if ves_arbyz > max:
        max = ves_arbyz
print(max, min)
