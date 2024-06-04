# Задача 2. Отгадать 2 числа, зная сумму и произведение

import os
os.system('cls')

numbers = [5, 6]

for a in range(0, 1001):
    for b in range(0, 1001):
        if a + b == numbers[0] and a * b == numbers[1]:
            res = [a, b]
               
print(res[1], res[0])

# p=int(input('Введите произведение X*Y: '))
# s= int(input ('Введите сумму X+Y: '))
# for i in range (1000):
#     if (s-i)*i==p and i<=(s-i):
#         print(i,s-i)

# while "Р" * i in string:
#     i += 1
# print(i - 1)
# print("Р" not in ["Р","О"])