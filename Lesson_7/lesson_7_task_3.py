# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найти в массиве медиану. Медианой
# называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в
# другой – не больше ее.Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте
# метод сортировки, который не рассматривался на уроках.
import random

m = int(input('Введите натуральное число m: '))
array = []
START = -100
FINISH = 100

for i in range(2 * m + 1):
    spam = random.randint(START, FINISH)
    array.append(spam)

median_index = len(array)//2

# Гномья сортировка


def gnome(array_):
    j = 1
    while j < len(array_):
        if not j or array_[j-1] <= array_[j]:
            j += 1
        else:
            array_[j], array_[j-1] =array_[j-1], array_[j]
            j -= 1
    return array_


print(array)
array = gnome(array)
print(array)
print(array[median_index])

