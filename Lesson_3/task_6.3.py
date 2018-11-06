# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный
# и максимальный элементы в сумму не включать.

import random

start = int(input('Введите начало диапазона,из которого необходимо генерировать числа: '))
finish = int(input('Введите конец этого диапазона: '))
quantity = int(input('Введите количество чисел,которые необходимо сгенерировать: '))


main_list = []
random_number = 0
max_number = start
min_number = finish
max_number_index = 0
min_number_index = 0
sum_ = 0


for i in range(0, quantity):
    random_number = random.randint(start, finish)
    main_list.append(random_number)
    if random_number > max_number:
        max_number = random_number
        max_number_index = i
    elif random_number < min_number:
        min_number = random_number
        min_number_index = i

if min_number_index < max_number_index:
    for i in range(min_number_index + 1, max_number_index):
        sum_ = sum_ + main_list[i]
elif min_number_index > max_number_index:
    for i in range(max_number_index + 1, min_number_index):
        sum_ = sum_ + main_list[i]

print(main_list)
print(f'Максимальный элемент массива {max_number} с индексом {max_number_index}.'
      f'Минимальный элемент массива {min_number} c индексом {min_number_index}')
print(f'Сумма элементов между ними равна = {sum_}')

