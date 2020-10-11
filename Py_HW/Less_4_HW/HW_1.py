from sys import argv


def calc(hours, rate, bonus):
    print("Заработная плата составит: ", hours*rate + bonus, " рублей.")


parameters = list(map(int, argv[1:]))
help_inf = 'Необходимы параметры: кол-во отработанных часов, почасовая ставка, премия'
if __name__ == '__main__':
    if len(argv) == 1:
        print(help_inf)
    elif len(argv) == 4:
        calc(parameters[0], parameters[1], parameters[2])


