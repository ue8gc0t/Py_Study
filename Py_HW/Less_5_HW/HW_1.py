with open('Task_1.txt', 'a') as f:
    while True:
        user_input = input(": ")
        if user_input == '':
            break
        else:
            f.writelines(user_input + '\n')