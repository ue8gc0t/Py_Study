user_str = input('Введите строку: ')
str_list = user_str.split()

i = 1
for item in str_list:
    print('№', i, ': ', item[:10:])
    i += 1
