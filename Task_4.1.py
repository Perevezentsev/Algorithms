import random

a = str(input('Выберите случаный генератор. Введите "i" в случае генератора целых чисел, "f" в случае вещественных чисел и "l" в случае букв: '))

if a == 'l':
    start = str(input('Введите первую букву диапазона: '))
    finish = str(input('Введите последнюю букву диапазона: '))
    print('Случайная буква:', chr(random.randint(ord(start), ord(finish))))

elif a == 'i':
    start = int(input('Введите первую цифру диапазона целых чисел: '))
    finish = int(input('Введите последнюю цифру диапазона целых чисел: '))
    print('Случайная цифра: ', random.randint(start, finish))
else:
    start = float(input('Введите первую цифру диапазона вещественных чисел: '))
    finish = float(input('Введите последнюю цифру диапазона вещественных чисел: '))
    print(f'Случайная цифра = {random.uniform(start, finish):.3f}')


