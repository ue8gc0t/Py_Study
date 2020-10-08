def my_func(num_1, num_2, num_3):
    my_list = sorted([num_1, num_2, num_3])
    return sum(my_list[1:])


print(my_func(12, 3, 19))
