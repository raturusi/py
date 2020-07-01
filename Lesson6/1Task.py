from time import sleep
from itertools import repeat
class TrafficLight:
    my_lightduration = {'red': 7, 'yellow': 2,  'green': 5}
    def running(self, color):
        print('\b'*20, end='')
        self.__color = color
        print(self.__color, end=' ')
        sleep(TrafficLight.my_lightduration.get(self.__color))
        print('Переключение', end='')
        sleep(0.5)


t = TrafficLight()
iterator = repeat(['red', 'yellow', 'green'], 5)
for i in range(5):
    my_light = next(iterator)
    for l in my_light:
        t.running(l)
