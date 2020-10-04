time_s = int(input("Enter time in seconds: "))

hours = time_s // 3600
minutes = (time_s % 3600) // 60
seconds = time_s % 60

print(f"{hours}:{minutes}:{seconds}")