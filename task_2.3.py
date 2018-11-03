# Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
# 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 0, 3, 4, 5, т.к. именно в этих позициях
#  первого массива стоят четные числа.
import random

start = int(input('Введите начало диапазона,из которого необходимо генерировать числа: '))
finish = int(input('Введите конец этого диапазона: '))
quantity = int(input('Введите количество чисел,которые необходимо сгенерировать: '))


main_list = []
even_indexes_list = []
random_number = 0

for i in range(0, quantity):
    random_number = random.randint(start, finish)
    main_list.append(random_number)
    if random_number % 2 == 0:
        even_indexes_list.append(i)

print(main_list)
print(even_indexes_list)
