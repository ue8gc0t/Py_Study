user_number = input("Enter number from 1 to 9: ")

count = 0
for i in range(1, 4):
    count += int(user_number * i)

print(count)