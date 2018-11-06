# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127 - м включительно.
# Вывод выполнить в табличной форме: по десять пар «код - символ» в каждой строке.

START = 32
FINISH = 127
a = ''
n = 0
for i in range(START, FINISH + 1):
    if i <= FINISH + 1 - FINISH % 10:
        a = a + str(i) + '-' + str(chr(i)) + '  '
        n += 1
        if n == 10:
            print(a)
            n = 0
            a = ''
    else:
        a = a + str(i) + '-' + str(chr(i)) + '  '
print(a)
