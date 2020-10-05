user_list = []

print('Заполните лист элементами, для завершения введите "exit"')
while True:
    user_item = input(': ')
    if user_item != 'exit':
        user_list.append(user_item)
    else:
        break

new_list = []
i = 0
while i < len(user_list):
    try:
        new_list.insert(i, user_list[i + 1])
        new_list.insert(i + 1, user_list[i])
        i += 2
    except IndexError:
        new_list.append(user_list[i])
        break

print(new_list)