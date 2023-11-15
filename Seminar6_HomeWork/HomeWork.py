# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

a1 = int(input("Enter the first element of the progression (a1): "))
d = int(input("Enter the common difference (d): "))
n = int(input("Enter the number of elements (n): "))

print(f'{[a1 + (i * d) for i in range(n)]}')

# print(f"result: {progression}")

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

list1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

min_value = int(input('input min value: '))
max_value = int(input('input max value: '))

# for i in range(len(list1)):
#     if min_value <= list1[i] <= max_value:
#         print(i, end=' ')

print([i for i in range(len(list1)) if min_value <= list1[i] <= max_value])
