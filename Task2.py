# Задача 2. Отгадать 2 числа, зная сумму и произведение

import os
os.system('cls')

numbers = [7, 12]
print(numbers)

for a in range(0, 1001):
    for b in range(0, 1001):
        if a + b == numbers[0] and a * b == numbers[1]:
            set = {a, b}
print(*set)
        
            

