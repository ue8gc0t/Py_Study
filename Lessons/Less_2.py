# print(abs(-5))    # Модуль числа
#
# print(5 & 3)    # 0101 * 0011 -> 0001 = 1
# print(5 & 3)    # 0101 + 0011 -> 0111 = 7
# print(5 ^ 3)    # 0101 ^ 0011 -> 0110 = 6
# print(6 >> 1)   # сдвиг вправо 6/2^1 = 3
# print(6 << 3)   # 6*2^3 = 48
# print(int("101101", 2)) # перевод в двоичную
# print(bin(17))  # oct() hex()
# print(complex(5, 6))
#
#
# my_str = 'Roman'
# print(my_str * 3)
# print(my_str[2]) [start: stop: step]
#
# my_str = 'grek skar'
# print(my_str.split('r'))
#
# print('_'.join(['G', 'ek ska', '']))
# print(my_str.capitalize())
# print(my_str.title())
# print(my_str.lower())
# print(my_str.upper())
#
# print('i' in my_str)
# print(my_str.count('a'))
# print(my_str.find('a', 4))
#
# my_list = ['Anvar', 'Irina', 510, False]
# my_list[1:2:3]
# my_list.append('Ivan')
# my_list.insert(2, 'Kiril')
# cutted = my_list.pop()
# my_list.reverse()
# my_list.index('Irina')
#
# my_tuple = ('Anvar', 'Irina', 510, False)   # Неизменяемый
# print(my_tuple)
#
# my_set = {1, 2, 3, 4, 3, 1, 7, 8, 9, 10}
# print(my_set)
#
# a = {1, 2, 3}
# b = {3, 4, 5}
#
# print(a | b)
# print(a & b)
# print(a ^ b)
# print(a - b)
#
# a.remove(9)
# a.discard(9)
#
# my_dict = {'name': 'Ivan', 'age': 50}
# print(my_dict.get('name1'))
# my_dict[5] = 'asd'
# print(my_dict)
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
#
# a = int(input("Number: "))
# try:
#     print(10 / a)
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# except ValueError:
#     print("ValueError")
#
# a = 10
# b = 10
#
# print(a is b)
# print(id(a))
# print(id(b))
#
# age = int(input("Age: "))
# print("Welcome" if age >= 18 else "No access")  # тернарный оператор
# a = 5 if age >= 18 else 8
# print(a)
#
# my_list = [1, 2, 3, 5, 6, 9]
# for i in my_list.copy():
#     my_list.remove(i)
# print(my_list)
#
# import copy
#
# a = [10, 20, 30, [300, 400]]
# b = copy.deepcopy(a)
# b[3].append(40)
#
# print(a)