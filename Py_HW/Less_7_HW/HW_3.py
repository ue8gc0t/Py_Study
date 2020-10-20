class Colony:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return self.count + other.count

    def __sub__(self, other):
        if self.count > other.count:
            return self.count - other.count
        else:
            print('Вычитание невозможно')

    def __mul__(self, other):
        return self.count * other.count

    def __truediv__(self, other):
        return int(self.count / other.count)

    @property
    def make_order(self):
        return ''.join([(lambda count: '*\n' if i % 5 == 0 else '*')(self.count) for i in range(1, self.count + 1)])


colony1 = Colony(35)
colony2 = Colony(16)

print(colony1 + colony2)
print(colony1 - colony2)
print(colony1 * colony2)
print(colony1 / colony2)

print(colony2.make_order)
