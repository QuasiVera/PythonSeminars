'''
Если мы перечислим все натуральные числа до 10, кратные 3 или 5, мы получим 3, 5, 6 и 9. Сумма этих кратных равна 23.
Завершите решение так, чтобы оно возвращало сумму всех чисел, кратных 3 или 5, меньше переданного числа. 
Кроме того, если число отрицательное, верните 0 (для языков, в которых они есть)
Примечание. Если число кратно и 3, и 5, считайте его только один раз .
'''

str1 = input('Введите строку  1: ')
str2 = input('Введите строку  2: ')
print(str1[(len(str1)-len(str2)):]==str2)
    



