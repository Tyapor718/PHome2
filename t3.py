# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
n= int (input ('Введите N'))
for i in range (1,n):
    if 2**i<n:
        print (2**i) 
      