proceeds = float(input("Введите значение выручки: "))
costs = float(input("Введите значение издержок: "))

if proceeds > costs:
    print("Фирма работает с прибылью")
    print("Рентабельность фирмы состовляет: ", proceeds / costs)
elif proceeds < costs:
    print("Фирма работает в убыток")
else:
    print("Фирма работает в 0")

employees = int(input("Введите количество сотрудников в вашей компании: "))
print("Прибыль фирмы в расчете на однго сотрудника равнв", proceeds / employees)
