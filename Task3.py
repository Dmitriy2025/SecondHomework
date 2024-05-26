# Задача 3. Вывести значения списка, со степенями 2, но меньшего введенного числа n

n = int(input('Введите число n: '))
origin_list = [0] * n
filtered_list =[]

for i in range(n):
    if 2 ** i < n:
        origin_list[i] = 2 ** i 

for value in origin_list:
    if value != 0:
        filtered_list.append(value)
print(*filtered_list)
