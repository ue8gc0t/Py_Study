from itertools import count, cycle

n = int(input('Введите целое число: '))
for el in count(n):
    if el > n + 20:
        break
    else:
        print(el)

two_steps_twice = ['Sun', 'side', 'dance', 'step', 'for', 'two']
i = 0
for el in cycle(two_steps_twice):
    if el == 'Sun':
        i += 1
    if i > 4:
        break
    else:
        print(el)
