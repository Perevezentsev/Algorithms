# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья
# прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
# Примечание: 4 квартала - это 4 разных прибыли ;-)

n = int(input('Введите количество предприятий :'))
companies = {}
sum_ = 0

for i in range(n):
    name = str(input(f'Введите название {str(i+1)} - го предприятия: '))
    fist_quarter = float(input(f'Введите прибыль {name} за первый квартал: '))
    second_quarter = float(input(f'Введите прибыль {name} за второй квартал: '))
    third_quarter = float(input(f'Введите прибыль {name} за третий квартал: '))
    fourth_quarter = float(input(f'Введите прибыль {name} за четвертый квартал: '))
    yearly_revenue = fist_quarter + second_quarter + third_quarter + fourth_quarter
    companies[name] = yearly_revenue
    sum_ = sum_ + yearly_revenue

average = sum_ / n

print(f'Средняя прибыль за год для введенных предприятий = {average:.2f}')
print(f'Годовая прибыль следующих предприятий меньше средней :')

for i in companies:
    if companies[i] < average:
        print(i)

print(f'Годовая прибыль следующих предприятий больше средней:')

for i in companies:
    if companies[i] > average:
        print(i)
