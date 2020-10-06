# a = [1, 2, 3, 4, 7]
#
# for i in enumerate(a, start=1):  # создает картеж
#     print(i)
#
# input().split()
#
# FUNCTIONS
# print(max(1, 2, 3))
# print(max('aaa', 'zz', key=len))
# print(round(1.2883, 3))
#
# def say_hello(name):
#     print(name, 'Hello')
#
# say_hello('Adel')
#
# def average(numbers):
#     count = len(numbers)
#     my_sum = sum(numbers)
#     answer = my_sum/ count
#     # print(answer)
#     return answer
#
#
# avg_num = average([1, 2, 3, 5, 7, 19])
# print(avg_num)
#
# def average(text):
#     pass
# average('qwe')
#
# def print(txt):     # Переопредление функции
#     pass
#
# x = 100
#
# def test():
#     print(x)
#
# x = 100
#
# def test():
#     global x
#     x = 99
#
# test()
#
#
# def my_fun(name, surname='Guest'):
#     print(name, surname)
#
#
# my_fun('Ivan', 'Ivanov')
# my_fun('Ivan')
#
# def my_fun(name, *data):    # *args
#     print(name, *data)
#
#
# my_fun('Ivan', 50)
# my_fun('Ivan', 70)
# my_fun('Ivan', 50, 70, 59, 10)
#
#
# def my_fun(name, surname, age):    # *args
#     print(name, surname, age)
#
#
# my_fun(name='Ivan', surname='Ivanov', age=50)   # Именованая передача значений
# def my_fun(name, **kwargs):    # *args
#     print(name, kwargs)
#
#
# my_fun(name='Ivan', surname='Ivanov', age=50)   # Именованая передача значений
#
# names = ['Olga', 'Irina', 'Zulichka', 'Ilya', 'Ivan']
# ages = [18, 20, 54, 19]
#
# for name, age in zip(names, ages):
#
#      print(name, age)
# print(dict(zip(names, ages)))   # Useful
#
#
# def my_pow(x):
#     return x ** 2 + 1
#
#
#
# result = list(map(my_pow, data))  # Useful
# print(result)
#
#
# def my_filter(num):
#     return num > 0
# print(list(filter(my_filter, data)))
#
# data = [2, 1, 5, -10, 39]
# print(list(filter(lambda x: x ** 2 + 1, data)))  # Useful
# print(list(filter(lambda x: x > 0, data)))  # Useful













