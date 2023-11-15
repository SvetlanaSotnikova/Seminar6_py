# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: 
# 7 
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)
# Вывод:
# 3 3 2 12

# list_1 = []
# size = int(input('input size of the first array: '))
# for el in range(size):
#     elem = int(input(f'input element {el + 1}: '))
#     list_1.append(elem)

# size = int(input('input size of the second array: '))
# list_2 = []
# for el in range(size):
#     elem = int(input(f'input element {el + 1}: '))
#     list_2.append(elem)

list_1 = [int(input(f'input element {el + 1}: ')) for el in range(int(input('input size of the first array: ')))]

list_2 = [int(input(f'input element {el + 1}: ')) for el in range(int(input('input size of the second array: ')))]

result_list = [elem for elem in list_1 if elem not in list_2]
print(result_list)

# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: 
# 5
# 1 2 3 4 5 
# Вывод: 
# 0
# Ввод:
# 1 5 1 5 1
# Вывод:
# 2

list_1 = [int(input(f'input element {el + 1}: ')) for el in range(int(input('input size of the first array: ')))]
print(list_1)

res_list = []
count = 0
for i in range(2, len(list_1)):
    if list_1[i - 1] > list_1[i] and list_1[i - 2] < list_1[i - 1]:
        res_list.append(list_1[i - 1])
        count += 1

print(f'{count} -> {res_list}')

res_list = [list_1[i - 1] for i in range(2, len(list_1)) if (lambda a, b, c: a > c and b < c)(list_1[i - 1], list_1[i], list_1[i - 2]) ]

# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: 
# 1 2 3 2 3 
# Вывод: 2

from typing import Counter

list_1 = [int(input(f'input element {el + 1}: ')) for el in range(int(input('input size of the first array: ')))]
print(list_1)

counter = Counter(list_1)

pair_count = sum(count // 2 for count in counter.values())

print(pair_count)

# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: 
# 300 
# Вывод:
# 220 284

import math

def sum_of_divisors(num):
    divisors = [1]
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            divisors.extend([i, num // i])
    return sum(divisors)

number = int(input('input number: '))
friendly_pairs = []

for num1 in range(3, number):
    num2 = sum_of_divisors(num1)
    if num2 > num1 and num2 <= number and sum_of_divisors(num2) == num1:
        friendly_pairs.append((num1, num2))

for pair in friendly_pairs:
    print(*pair)

# def sum_of_divisors(num):
#     return sum([1] + [i + num // i for i in range(2, int(num**0.5) + 1) if num % i == 0])

# number = int(input('input number: '))

# friendly_pairs = [(num1, num2) for num1 in range(3, number) for num2 in range(num1 + 1, number) if num2 > num1 and sum_of_divisors(num1) == num2 and sum_of_divisors(num2) == num1]

# for pair in friendly_pairs:
#     print(*pair)

