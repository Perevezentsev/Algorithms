# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
# Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

a = str(input('Введите шестнадцатиричное число: ')).upper()
b = str(input('Введите второе шестнадцатиричное число: ')).upper()

a_list = deque()
b_list = deque()
sum_ = deque()
translation_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
reverse_translation_dict = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8',
                            '9': '9', '10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
range1 = 0

# Разбиваем строки на символы и помещаем в очереди

for char in a:
    a_list.append(char)

for char in b:
    b_list.append(char)

print(a_list)
print(b_list)

# Если в одной из очередей больше символов, то в меньшей очереди добиваем разницу 0

if len(a_list) - len(b_list) < 0:
    for i in range(len(a_list), len(b_list)):
        a_list.appendleft('0')
elif len(a_list) - len(b_list) > 0:
    for i in range(len(b_list), len(a_list)):
        b_list.appendleft('0')

a_list.reverse()
b_list.reverse()

# Переводим 16-е символы в 10-е с помощью словаря и производим сложение посимвольно в 16-й системе

for i in range(len(a_list)):
    spam = translation_dict[a_list[i]] + translation_dict[b_list[i]] + range1
    range1 = 0
    if spam > 15:
        sum_.append(str(spam % 16))
        range1 += 1
    else:
        sum_.append(str(spam))

if range1 == 1:
    sum_.append(str(1))

# Переводим 10-е символы в 16 с помощью обратного словаря

for i in range(len(sum_)):
    for key in reverse_translation_dict:
        if sum_[i] == key:
            sum_[i] = reverse_translation_dict[key]

sum_.reverse()

print(f'Сумма введенных цифр =  {sum_}')

# **********************************************************************************************************************
# Умножение

multiplication = deque()
multiplication_sum = deque()
multiplication_sums = {}
range2 = 0
range3 = 0

# Переводим из 16-х в 10-е и производим умножение кадого числа в одном массиве на все числа во втором. Промежуточные
#  суммы  multiplication_sum сохраняем в словаре multiplication_sums
for i in range(len(a_list)):
    range2 = 0
    for j in range(len(b_list)):
        spam = translation_dict[a_list[i]] * translation_dict[b_list[j]] + range2
        range2 = 0
        if spam > 15:
            multiplication_sum.append(reverse_translation_dict[str(spam % 16)])
            range2 = spam // 16
        else:
            multiplication_sum.append(reverse_translation_dict[str(spam)])
    if range2 != 0:
        multiplication_sum.append(reverse_translation_dict[str(range2)])
    multiplication_sums[i] = multiplication_sum
    multiplication_sum = deque()

# Сдвигаем суммы по разрядам и забиваем в сдвинутые суммы 0
for key in multiplication_sums:
    spam = key
    while spam != 0:
        multiplication_sums[key].appendleft('0')
        spam -= 1

# Присваиваем переменной multiplication значению 0 ключа из словаря multiplication_sums
multiplication = multiplication_sums[0]

# Производим сложение сумм из словаря и сохраняем в значении multiplication
for key in range(1, len(multiplication_sums)):
    spam1 = multiplication_sums[key]
    while len(multiplication) < len(spam1):
        multiplication.append('0')
    for i in range(len(spam1)):
        spam = translation_dict[multiplication[i]] + translation_dict[spam1[i]] + range3
        range3 = 0
        if spam > 15:
            multiplication[i] = (reverse_translation_dict[str(spam % 16)])
            range3 += 1
        else:
            multiplication[i] = (reverse_translation_dict[str(spam)])

if range3 != 0:
    multiplication.append(str(1))

# Переводим 10-е символы в 16-е с помощью обратного словаря
for i in range(len(multiplication)):
    for key in reverse_translation_dict:
        if multiplication[i] == key:
            multiplication[i] = reverse_translation_dict[key]

multiplication.reverse()

while multiplication[0] == '0':
    if len(multiplication) != 1:
        multiplication.popleft()
    else:
        multiplication = ['0']
        break

print(f'Произведение введенных цифр =  {multiplication}')
