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
print(f'Количество четных цифр: {b}')
print(f'Количество нечетных цифр: {c}')
