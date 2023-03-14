def GetUserNumber(message_to_user):
    flag = True
    while flag:
        try:
            print(message_to_user)
            n = int(input())
            if n or n==0:
                flag = False
                return n
            #else:
                #print('Ошибка ввода! Введено ')
        except ValueError:
            print('Ошибка ввода! Введено не число')

def Fibonaci(num):
    if num<=1:
        return num
    else:
        return Fibonaci(num-1)+Fibonaci(num-2)



a = GetUserNumber('Введите число: ')
print(Fibonaci(a))


