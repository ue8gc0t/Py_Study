with open('Task_4_1.txt', 'r') as f:
    data = list(map(lambda a: a.split(), f.readlines()))

with open('Task_4_2.txt', 'w') as f:
    for i in data:
        if i[0] == 'One':
            f.writelines('Один - 1\n')
        elif i[0] == 'Two':
            f.writelines('Два - 2\n')
        elif i[0] == 'Three':
            f.writelines('Три - 3\n')
        elif i[0] == 'Four':
            f.writelines('Четыре - 4')
