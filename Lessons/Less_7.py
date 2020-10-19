class Car:
    def __init__(self):
        self.modules = []
        self.f_c = 7

    def __add__(self, module):
        self.modules.append(module)
        return self     # Возоащает не NoneType

    def __str__(self):
        return f'{self.modules}'

    def __setattr__(self, key, value):
        # super().__setattr__(key, value)
        self.__dict__[key] = value
        print(f'создаем модуль {key} - {value}')

    def __getitem__(self, item):
        return self.modules[item]

    def __call__(self, price):
        print(f'Car {self.model} {price}')

    def __eq__(self, other):
        return self.f_c == other

    def __del__(self):
        print('delete obj')

#
# module1 = 'теплый руль'
# module2 = 'теплое сидение'
# module3 = 'меховые педальки'
#
# car = Car()

# car.modules.append(module1)
# car.modules.append(module2)
# car.modules.append(module3)
#
# car + module1   # __add__
# car + module2
# car + module3
#
# print(car)  # __str__
#
# car.model = 'Tesla.Y'
# print(car[1])
# car(price=1000)
#
# print(car == 7)
#
#
# from abc import ABC, abstractmethod
#
#
# class MyAbcClass(ABC):
#     @abstractmethod
#     def my_method1(self):
#         pass
#
#     @abstractmethod
#     def my_method2(self):
#         pass
#
#
# class MyClass(MyAbcClass):
#     def my_method1(self):
#         pass
#
#     def my_method2(self):
#         pass
#
#
# myclass = MyClass()
#
# for i in [1, 2, 3, 4, 5]:
#     print(i)
#
# class Iterator:
#     def __init__(self):
#         self.i = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i <= 5:
#             return self.i
#         else:
#             raise StopIteration
#
#
# qwe = Iterator()
# for i in qwe:
#     print(i)
#
#
# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self._age = age
#
#     @property
#     def age(self):
#         return self._age
#
#
# human = Human('Ivan', 40)
# print(human.age)

class WinDoor:
    def __init__(self, wd_l, wd_h ):
        self.square = wd_h * wd_l


class Room:
    def __init__(self, l1, l2, h):
        self.square = 2 * h * (l1 + l2)
        self.wd = []

    def add_windoor(self, wd_l, wd_h):
        self.wd.append(WinDoor(wd_l, wd_h))

    def common_square(self):
        main_square = self.square
        for el in self.wd:
            main_square -= el.square
        return main_square
