from itertools import count
from time import sleep


def generator():
    factorial = 1
    for i in count(1):
        factorial *= i
        yield factorial


g = generator()
for el in g:
    print(el)
    sleep(2)