class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self, hours):
        return self._income['wage'] * hours + self._income['bonus']


worker = Position('Ivan', 'Ivanov', 'storekeeper', 72, 8000)
print(worker.get_full_name())
print(worker.get_total_income(178))
