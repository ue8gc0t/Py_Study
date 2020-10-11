# import Py_HW.Less_3_HW.HW_1 as hw
# from Py_HW.Less_3_HW.HW_1 import division
# from Py_HW.Less_3_HW.HW_1 import *
import time
import sys
import math
import os
# print(division(50, 10))


# print(time.localtime())     # начало эпохи
# print(time.time())
#
# a = time.time()
#
# for i in range(10, 10000000):
#     pass
# b = time.time()
#
# print(b - a)
#
# print('Hello')
#
# time.sleep(2)
#
# print(2)

# print(math.pi)
# print(math.floor(2.9))
# print(math.ceil(2.9))

# for i in sys.path:
#     print(i)
#
# print(sys.argv)
# print('qwe')
#
# params = sys.argv[1:]
# if 'h' in params:
#     print('adaddad')

# import argparse     # Важно


# print(os.getcwd())

# my_list = [1, 2, 3, 4, 5, 6, 20]
# new_list = [x ** 2 for x in my_list if x % 2 == 0]
# print(new_list)
# new_dict = {x: x ** 2 for x in my_list if x % 2 == 0}
# print(new_dict)

# yield

# def generator():
#     i= -2
#     while True:
#         i += 1
#         yield i
#
# g = generator()

# import random
#
# print(random.random())
# print(random.randint(1, 20))
# print(random.randrange(1, 20, 4)
from functools import reduce, partial

# def my_f(num1,num2):
#     return num1 ** num2

# print(reduce(my_f, [10, 20, 30]))

# from itertools import count, cycle
#
# colors = ['green', 'yellow', 'red', 'yellow']
# for i in cycle(colors):
#     print(i)