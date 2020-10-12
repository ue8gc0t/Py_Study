my_list = [12, 3, 53, 55, 23, 1, 3, 55, 3, 23, 46, 129, 19]
new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]

print(new_list)