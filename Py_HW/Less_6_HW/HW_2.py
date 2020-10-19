class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calc(self):
        return self.__width * self.__length * 25 * 1


road = Road(2, 3)
print(road.calc())