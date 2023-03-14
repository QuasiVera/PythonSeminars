'''
Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

'''
num = int(input('Введите число: '))

def IsSimple(num):
   
    for i in range(2,num//2):
        if num%i == 0:
            print('Число не простое')
            return  
    if num <=1:
        print('Число ни простое ни составное ')
    else:
        print('Число простое')

IsSimple(num)
