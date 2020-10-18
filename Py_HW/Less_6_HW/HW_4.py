class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Wrmwrm')

    def stop(self):
        print('Iieihhh')

    def turn(self, direction):
        print(f'Turning {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Вы превышаете скорость')
        else:
            print(self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Вы превышаете скорость')
        else:
            print(self.speed)


class PoliceCar(Car):
    pass


town_car = TownCar(45, 'blue', 'Mazda', False)
sport_car = SportCar(120, 'red', 'Porsche', False)
work_car = WorkCar(55, 'brown', 'Sedan', False)
police_car = PoliceCar(55, 'white', 'Sedan', True)

print(police_car.is_police)
print(sport_car.color)
print(work_car.name)

town_car.go()
work_car.show_speed()
town_car.show_speed()
sport_car.turn('Right')
police_car.stop()