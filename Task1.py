# Определить минимальное количество монеток, которое нужно перевернуть

# n = ввести 

import os
import random

os.system('cls')

rowLength = int(input('Введите длинну списка: '))
coins = [random.randint(0, 1) for i in range(rowLength)]
sumzero = 0
sumone = 0

print(coins)

for i in coins:
    if i == 0: sumzero += 1
    else: sumone += 1

if sumzero <= sumone: print(sumzero)
else: print(sumone)
