with open('Task_5.txt', 'w+') as f:
    f.write(input('Введите последовательность чисел, разделенных пробелом: '))
    f.seek(0)
    data = f.read()
    print(sum(map(int, data.split())))