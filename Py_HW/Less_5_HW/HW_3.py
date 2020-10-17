with open('Task_3.txt', 'r') as f:
    data = list(map(lambda a: a.split(), f.readlines()))
    m_sum = 0
    for i in data:
        if int(i[1]) < 20000:
            print(i[0])
        m_sum += int(i[1])
    print('average = ', round(m_sum / len(data), 2))

