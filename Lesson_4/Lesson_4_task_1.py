# Проанализировать скорость и сложность одного из любых алгоритмов, разработанных в рамках домашнего задания первых
# трех уроков.

# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

import cProfile


# 1. Рекурсия


def func(n):
    if n == 0:
        return 0
    else:
        b = (-0.5) ** (n - 1) + func(n - 1)
        return b


# \Lesson_4>python -m timeit -n 1000 -s "import Lesson_4_task_1" "Lesson_4_task_1.func(10)"
# 1000 loops, best of 5: 7.74 usec per loop
# \Lesson_4>python -m timeit -n 1000 -s "import Lesson_4_task_1" "Lesson_4_task_1.func(100)"
# 1000 loops, best of 5: 70.6 usec per loop
# \Lesson_4>python -m timeit -n 1000 -s "import Lesson_4_task_1" "Lesson_4_task_1.func(500)"
# 1000 loops, best of 5: 396 usec per loop

# cProfile.run('func(10)') 11/1    0.000    0.000    0.000    0.000 Lesson_4_task_1.py:11(func)
# cProfile.run('func(100)') 101/1    0.000    0.000    0.000    0.000 Lesson_4_task_1.py:11(func)
# cProfile.run('func(500)') 501/1    0.002    0.000    0.002    0.002 Lesson_4_task_1.py:11(func)

# Зависимость между количеством n и временем выполнения практически линейная. Количество циклов при увеличении n также
# растет

# 2. Рекурсия + словарь

def func_dict(n):
    func_d = {0: 0}

    def _func_dict(n):
        if n in func_d:
            return func_d[n]
        func_d[n] = (-0.5) ** (n - 1) + _func_dict(n - 1)
        return func_d[n]

    return _func_dict(n)


# \Lesson_4>python -m timeit -n 1000 -s "import Lesson_4_task_1" "Lesson_4_task_1.func_dict(10)"
# 1000 loops, best of 5: 11.6 usec per loop
# \Lesson_4>python -m timeit -n 1000 -s "import Lesson_4_task_1" "Lesson_4_task_1.func_dict(100)"
# 1000 loops, best of 5: 97.6 usec per loop
# \Lesson_4>python -m timeit -n 1000 -s "import Lesson_4_task_1" "Lesson_4_task_1.func_dict(500)"
# 1000 loops, best of 5: 529 usec per loop

# cProfile.run('func_dict(10)')  11/1    0.000    0.000    0.000    0.000 Lesson_4_task_1.py:38(_func_dict)
# cProfile.run('func_dict(100)') 101/1    0.000    0.000    0.000    0.000 Lesson_4_task_1.py:38(_func_dict)
# cProfile.run('func_dict(500)') 501/1    0.003    0.000    0.003    0.003 Lesson_4_task_1.py:38(_func_dict)

# В этом случае тоже линейная зависимость между n и временем выполнения/количеством циклов. Но время выполнения больше,
# чем в варианте №1. Поэтому словари в данной задаче не имеет смысла использовать.


# 3. Цикл


def func_loop(n):
    item = 1
    sum_ = 0

    for _ in range(n):
        sum_ += item
        item /= -2
    return sum_

# \Lesson_4>python -m timeit -n 1000 -s "import Lesson_4_task_1" "Lesson_4_task_1.func_loop(10)"
# 1000 loops, best of 5: 2.5 usec per loop
# \Lesson_4>python -m timeit -n 1000 -s "import Lesson_4_task_1" "Lesson_4_task_1.func_loop(100)"
# 1000 loops, best of 5: 15.4 usec per loop
# \Lesson_4>python -m timeit -n 1000 -s "import Lesson_4_task_1" "Lesson_4_task_1.func_loop(500)"
# 1000 loops, best of 5: 82.4 usec per loop

# cProfile.run('func_loop(10)') 1    0.000    0.000    0.000    0.000 Lesson_4_task_1.py:64(func_loop)
# cProfile.run('func_loop(100)') 1    0.000    0.000    0.000    0.000 Lesson_4_task_1.py:64(func_loop)
# cProfile.run('func_loop(500)') 1    0.000    0.000    0.000    0.000 Lesson_4_task_1.py:64(func_loop)

# Также линейная зависимость. Но данный вариант выполняется гораздо быстрее 82.4 usec vs. 396 usec  в Варианте № 1.
# Плюс сама функция вызывается только 1 раз. Поэтому оптимальным вариантом решения является 3-й
