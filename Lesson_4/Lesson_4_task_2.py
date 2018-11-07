# Написать два алгоритма нахождения i-го по счёту простого числа. Первый - без использования "решета"
# Второй -использовать алгоритм решето Эратосфена. Проанализировать скорость и сложность алгоритмов.

import cProfile


# a = int(input('Введите какое по счету простое число необходимо найти: '))


def search_for_simple(n):
    list_of_simple_digits = [2]
    candidate = 2

    while len(list_of_simple_digits) != n:
        candidate += 1
        for i in list_of_simple_digits:
            if candidate % i == 0:
                break
        else:
            list_of_simple_digits.append(candidate)
    return list_of_simple_digits[-1]


# print(search_for_simple(a))

# \Lesson_4>python -m timeit -n 1000 -s "import Lesson_4_task_2" "Lesson_4_task_2.search_for_simple(10)"
# 1000 loops, best of 5: 15.9 usec per loop
# \Lesson_4>python -m timeit -n 1000 -s "import Lesson_4_task_2" "Lesson_4_task_2.search_for_simple(100)"
# 1000 loops, best of 5: 678 usec per loop
# \Lesson_4>python -m timeit -n 1000 -s "import Lesson_4_task_2" "Lesson_4_task_2.search_for_simple(500)"
# 1000 loops, best of 5: 15.3 msec per loop

# cProfile.run('search_for_simple(10)') 28    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# cProfile.run('search_for_simple(100)')   540    0.001    0.000    0.001    0.000 {built-in method builtins.len}
# cProfile.run('search_for_simple(500)') 3570    0.004    0.000    0.004    0.000 {built-in method builtins.len}

# При увеличении n время выполнения и количество циклов растут нелинейно. Больше всего раз выполняется вычисление длины
# списка


# a = int(input('Введите какое по счету простое число необходимо найти: '))


def sieve_func(n):
    sieve = [0, 0, 2]
    candidate = 2
    spam = 1

    while spam != n:
        candidate += 1

        for i in range(2, candidate):
            if candidate % i == 0:
                sieve.append(0)
                break
        else:
            sieve.append(candidate)
            spam += 1

    res = [i for i in sieve if i != 0]
    return res[-1]


# print(sieve_func(a))

# \Lesson_4>python -m timeit -n 1000 -s "import Lesson_4_task_2" "Lesson_4_task_2.sieve_func(10)"
# 1000 loops, best of 5: 36.2 usec per loop

# \Lesson_4>python -m timeit -n 1000 -s "import Lesson_4_task_2" "Lesson_4_task_2.sieve_func(100)"
# 1000 loops, best of 5: 2.92 msec per loop

# \Lesson_4>python -m timeit -n 1000 -s "import Lesson_4_task_2" "Lesson_4_task_2.sieve_func(500)"
# 1000 loops, best of 5: 105 msec per loop

# cProfile.run('sieve_func(10)') 27    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# cProfile.run('sieve_func(100)') 539    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
# cProfile.run('sieve_func(500)')  3569    0.004    0.000    0.004    0.000 {method 'append' of 'list' objects}

# В данном случае второй алгоритм работает дольше , хотя для нахождения заданного простого числа ему и требуется на 1
# цикл меньше .Поэтому решето Эратосфена эффективнее при нахождении простых чисел до какого-то конкретного числа.
# В случае нахождения конкретного по счету простого числа лучше использовать обычный алгоритм перебора.
# Например, вариант 1.