
#======================== Возведение в степень рекурсией =================

def Pow1(a):
    sum =0
    while a>0:
        sum+=a%10
        a=a//10
    if sum<10: return sum
    return Pow1(sum)

# def Rec(a):
#     if Pow1(a)<9: return Pow1(a)
#     return Rec(Pow1(a))

#========================= Ввод данных ==================

def GetUserNumber(message_to_user):
    flag = True
    while flag:
        try:
            print(message_to_user)
            n = int(input())
            if n or n==0:
                flag = False
                return n
        except ValueError:
            print('Ошибка ввода! Введено не число')



#===============================

a = GetUserNumber('Введите число A: ')

print(f' {a} = {Pow1(a)}')
print(Pow1(a))
