def str_sum():
    num_sum = 0
    while True:
        num_list = input("Enter numbers separated by a space, to exit enter 'Q'\n:  ").split()
        if num_list[0] == 'Q' or num_list[0] == 'q':
            break
        if 'Q' or 'q' in num_list:
            num_sum += sum(map(int, num_list[:-1]))
            print(num_sum)
            break
        else:
            num_sum += sum(map(int, num_list))
            print(num_sum)
    return


str_sum()
