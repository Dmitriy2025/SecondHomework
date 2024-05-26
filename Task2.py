# Задача 2. Отгадать 2 числа, зная сумму и произведение

import os
os.system('cls')

numbers = [5, 6]
print(numbers)

for a in range(0, 1001):
    for b in range(0, 1001):
        if a + b == numbers[0] and a * b == numbers[1]:
            res = [a, b]
            
print(res[1], res[0])
