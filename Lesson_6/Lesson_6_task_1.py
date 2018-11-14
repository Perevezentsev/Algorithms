# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.Для анализа возьмите
# любые 1-3 ваших программы. Результаты анализа вставьте в виде комментариев к коду.
# P.S. Напишите в комментариях версию Python и разрядность ОС

# **********************************************************************************************************************
import sys
import random

# Задача №1
# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3
# четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

a = int(input('Введите число: '))
b = 0
c = 0
if a == 0:
    b += 1
while a != 0:
    if a % 10 % 2 == 0:
        b += 1
    else:
        c += 1
    a = a // 10
# print(f'Количество четных цифр: {b}')
# print(f'Количество нечетных цифр: {c}')


# Функция расчета объема занимаемой памяти

def get_size(x):
    size_ = sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                size_ = size_ + get_size(key)
                size_ = size_ + get_size(value)
        elif not isinstance(x, str):
            size_ = sys.getsizeof(x)
            for item in x:
                size_ = size_ + get_size(item)

    return size_


# Расчет объема занимаемой памяти

variables1 = (a, b, c)
size1 = 0

for var in variables1:
    size1 = size1 + get_size(var)

print(f'Объём памяти, выделенный под переменные в задаче №1 , составляет {size1} байт')

# Задача №2
# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127 - м включительно.
# Вывод выполнить в табличной форме: по десять пар «код - символ» в каждой строке.

START = 32
FINISH = 127
d = ''
n = 0
for i in range(START, FINISH + 1):
    if i <= FINISH + 1 - FINISH % 10:
        d = d + str(i) + '-' + str(chr(i)) + '  '
        n += 1
        if n == 10:
            # print(d)
            n = 0
            d = ''
    else:
        d = d + str(i) + '-' + str(chr(i)) + '  '
# print(d)

# Расчет объема занимаемой памяти


variables2 = (START, FINISH, d, n, i)
size2 = 0

for var in variables2:
    size2 = size2 + get_size(var)

print(f'Объём памяти, выделенный под переменные в задаче №2, составляет {size2} байт')

# Задача №3

# Определить, какое число в массиве встречается чаще всего.

START2 = 100
FINISH2 = 1000
QUANTITY = 100

main_list = []
random_number = 0
max_frequency = 0
max_frequency_digit = 0
n_ = 0

for k in range(0, QUANTITY):
    random_number = random.randint(START2, FINISH2)
    main_list.append(random_number)

for l in range(0, len(main_list)):
    for j in range(0, len(main_list)):
        if main_list[l] == main_list[j]:
            n_ += 1
    if n_ > max_frequency:
        max_frequency = n_
        max_frequency_digit = main_list[l]
    n_ = 0

# print(main_list)
# print(f'В данномм массиве чаще всего встречается число {max_frequency_digit}. Количество повторений {max_frequency}')

# Расчет объема занимаемой памяти

variables3 = (START2, FINISH2, QUANTITY, main_list, max_frequency, max_frequency_digit, n_, k, j, l, random_number)
size3 = 0

for var in variables3:
    size3 = size3 + get_size(var)

print(f'Объём памяти, выделенный под переменные в задаче №3, составляет {size3} байт')

# 64-разрядная операционная система. Python 3.7.1
# Меньше  всего места выделено под переменные в задаче №1, т.к. в ней используются переменные типа Int и их всего 3 шт.
# В задаче №2  используются переменные типа Int и константы, но их больше,чем в задаче №1, поэтому и места выделяется
# больше.
# В задаче №3 уже встречаются списки, под которые выделяется гораздо больше памяти.
