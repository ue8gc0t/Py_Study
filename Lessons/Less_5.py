# f = open('text.txt')
#
# lines = f.readlines()
# print(lines)
# for line in lines:
#     print(line.strip())     # Более оптимальный
#     # print(line, end='')
#
# line = f.readline()
# f.close()
#
# file = open('test1.txt', 'w')
# file.write('qwe\nasdad\ndas')
# file.writelines(['asdasd\n', 'dassd\n', 'sad'])
# file.close()
#
#
# file = open('test1.txt', 'w')
# file.write('qwe\nasdad\ndas')
# a = file.read()
# print(a)
# file.close()
#
# f = open('text.txt', 'w')
# f.write('Hello')
# print('Hello', file=f)
# f.close()
#
# with open('text.txt', 'w') as file:     # Важно
#     file.write('Hello')
#     print(file.mode)
#     print(file.closed)
#
# with open('text.txt', 'w+') as f:
#     f.write('Petr\nVova\nFrack')
#     # f.seek(0)
#     # print(f.tell())
#     # print(f.read())
#     # print(f.tell())
#
# import os
# print(os.path.isdir('text.txt'))
#
import json


data = {'lol': 'kek'}

with open('test.json', 'w', ) as f_json:
    json.dump(data, f_json, indent=2)

# with open('test.json') as f_json:
#     data = json.load(f_json)

print(data)






