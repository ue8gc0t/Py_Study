with open('Task_6.txt', 'r') as f:
    data = {}
    for i in f.readlines():
        p_sum = 0
        for j in i.split()[1:]:
            if j != '—':
                p_sum += int(j.split('(')[0])
            else:
                pass
        data[i.split()[0][:-1:]] = p_sum
    print(data)