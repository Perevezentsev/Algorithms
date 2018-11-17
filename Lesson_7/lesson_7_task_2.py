# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
# [0; 50). Выведите на экран исходный и отсортированный массивы.
import random

array = []
VOLUME = 10

for i in range(VOLUME):
    spam = random.random()*50
    array.append(spam)
print(array)


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    result += left
    result += right
    return result


def mergesort(array_):
    left = []
    right = []
    if len(array_) < 2:
        return array_
    middle = len(array_) // 2
    for a in range(middle):
        left.append(array_[a])
    for b in range(middle, len(array_)):
        right.append(array_[b])
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)


print(mergesort(array))
