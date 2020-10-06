user_number = input("Enter number: ")

max_number = 0
i = 0

while True:
    if int(user_number) > 0:
        if int(user_number) % 10 > max_number:
            max_number = int(user_number) % 10
            user_number = str(int(user_number) // 10)
        else:
            user_number = str(int(user_number) // 10)
    else:
        break


# while i < len(user_number):
#     if int(user_number[i]) > max_number:
#         max_number = int(user_number[i])
#     i += 1


# for n in user_number:
#     if int(n) > max_number:
#         max_number = int(n)

print(max_number)
