from time import sleep
from itertools import cycle


class TrafficLight:
    _color = ['Red', 'Yellow', 'Green']
    _sleep_time = [7, 2, 10]

    def running(self):
        for i in cycle(zip(TrafficLight._color, TrafficLight._sleep_time)):
            print(i[0])
            sleep(i[1])


traffic_light = TrafficLight()
traffic_light.running()


