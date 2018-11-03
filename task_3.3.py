# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

start = int(input('Введите начало диапазона,из которого необходимо генерировать числа: \n'))
finish = int(input('Введите конец этого диапазона: \n'))
quantity = int(input('Введите количество чисел,которые необходимо сгенерировать: \n'))


main_list = []
random_number = 0
max_number = start
min_number = finish
max_number_index = 0
min_number_index = 0


for i in range(0, quantity):
    random_number = random.randint(start, finish)
    main_list.append(random_number)
    if random_number > max_number:
        max_number = random_number
        max_number_index = i
    elif random_number < min_number:
        min_number = random_number
        min_number_index = i

print(f'{main_list} \n')
print(f'Максимальное число: {max_number} с индексом {max_number_index} \n')
print(f'Минимальное число: {min_number} с индексом {min_number_index} \n')

main_list[max_number_index] = min_number
main_list[min_number_index] = max_number

print(main_list)

