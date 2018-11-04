# Определить, какое число в массиве встречается чаще всего.
import random

start = int(input('Введите начало диапазона,из которого необходимо генерировать числа: '))
finish = int(input('Введите конец этого диапазона: '))
quantity = int(input('Введите количество чисел,которые необходимо сгенерировать: '))

main_list = []
random_number = 0
max_frequency = 0
max_frequency_digit = 0
n = 0

for i in range(0, quantity):
    random_number = random.randint(start, finish)
    main_list.append(random_number)

for i in range(0, len(main_list)):
    for j in range(0, len(main_list)):
        if main_list[i] == main_list[j]:
            n += 1
    if n > max_frequency:
        max_frequency = n
        max_frequency_digit = main_list[i]
    n = 0

print(main_list)
print(f'В данномм массиве чаще всего встречается число {max_frequency_digit}. Количество повторений {max_frequency}')