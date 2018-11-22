# Определение количества различных подстрок с использованием хеш-функции. Пусть дана строка S длиной N. Например,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке. Для решения
# задачи рекомендую воспользоваться алгоритмом sha1 из модуля hashlib или встроенную функцию hash()

a = str(input('Введите строку: '))


def substring_counter(string):
    hash_lst = []
    for i in range(1, len(string)):
        for j in range(len(string)-i + 1):
            if hash(string[j:j+i]) not in hash_lst:
                hash_lst.append(hash(string[j:j+i]))

    return len(hash_lst)


print(substring_counter(a))






