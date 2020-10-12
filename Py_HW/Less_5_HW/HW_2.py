with open('Task_2.txt', 'r') as f:
    new_list = f.readlines()
    for i in range(0, len(new_list)):
        print('Строка №', i + 1, ': ', len(new_list[i].split()))


        