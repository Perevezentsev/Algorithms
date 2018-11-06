# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

start = int(input('Введите начало диапазона,из которого необходимо генерировать числа: '))
finish = int(input('Введите конец этого диапазона: '))
quantity = int(input('Введите количество чисел,которые необходимо сгенерировать: '))

main_list = []
random_number = 0
max_number = start
max_number_index = 0
n = 0

for i in range(0, quantity):
    random_number = random.randint(start, finish)
    main_list.append(random_number)

for i in range(0, len(main_list)):
    if main_list[i] < 0:
        if main_list[i] > max_number:
            max_number = main_list[i]
            max_number_index = i

print(main_list)
print(f'В данномм массиве максимальный отрицательный элемент {max_number}. Позиция в массиве {max_number_index}')