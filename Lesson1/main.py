

n = int(input('Введите число км в день: '))
m = int(input('Введите расстояние: '))

t = m//n  # t=v/s
print(f'Доедем за {t+ bool(m%n)} дней')

s = (m + n - 1) // n 
print(s)
