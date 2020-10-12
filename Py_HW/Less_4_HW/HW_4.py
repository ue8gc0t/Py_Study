my_list = [12, 3, 53, 55, 23, 1, 3, 55, 3, 3, 23, 46, 129, 19]

new_list = [my_list[i] for i in range(0, len(my_list)) if not(my_list[i] in my_list[i + 1:] + my_list[0:i])]
print(new_list)