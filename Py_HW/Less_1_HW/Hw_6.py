a = float(input("Введите результат первого дня в километрах: "))
b = float(input("Введите желаемый результат в километрах: "))

i = 1
while a <= b:
    print(f"{i}-й день: {a:.2f} км")
    a += a*0.1
    i += 1
print(f"{i}-й день: {a:.2f} км")

print("")

print(f"На {i}-й день спортсмен достиг результата — не менее {b} км.")
