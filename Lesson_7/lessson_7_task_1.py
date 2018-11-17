# Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Вывести на экран исходный и отсортированный массивы.
import random

array = [i for i in range(-100, 100)]
random.shuffle(array)
print(array)


# Код с урока  с правильным знаком (сортировка по убыванию)

def bubble_default(array_):
    n = 1
    while n < len(array_):
        for i in range(len(array_) - 1):
            if array_[i] < array_[i + 1]:
                array_[i], array_[i + 1] = array_[i + 1], array_[i]
        n += 1
    return array_


print(bubble_default(array))


# Решение


def bubble(array_):
    n = 1
    while n < len(array_):
        counter = 0
        for i in range(len(array_) - n):
            if array_[i] < array_[i + 1]:
                array_[i], array_[i + 1] = array_[i + 1], array_[i]
                counter += 1
        if counter == 0:
            break
        n += 1
    return array_


print(bubble(array))
