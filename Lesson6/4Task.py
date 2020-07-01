class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} {self.name} start go with speed = {self.speed}')
    def stop(self):
        print(f'{self.color} {self.name} stopped')
    def turn(self, direction):
        print(f'{self.color} {self.name} turn {direction}')
    def show_speed(self):
        print(f'Speed = {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Speed = {self.speed}, overspeed, max speed = 60')
            self.speed = 60
        else:
            print(f'Speed = {self.speed}')
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Speed = {self.speed}, overspeed, max speed = 40')
            self.speed = 40
        else:
            print(f'Speed = {self.speed}')
class PoliceCar(Car):
    pass

c = Car(70, 'red', 'lada', bool())
print(str(c.speed) + ' ' + c.color+' ' + c.name+' ' + str(c.is_police))
c.go()
c.turn('right')
c.show_speed()
c.stop()

c = TownCar(65, 'yellow', 'TownCar', bool())
print(str(c.speed) + ' ' + c.color+' ' + c.name+' ' + str(c.is_police))
c.go()
c.turn('left')
c.show_speed()
c.show_speed()
c.stop()

c = SportCar(100, 'brown', 'SportCar', bool())
print(str(c.speed) + ' ' + c.color+' ' + c.name+' ' + str(c.is_police))
c.go()
c.turn('forward')
c.show_speed()
c.stop()

c = WorkCar(45, 'white', 'WorkCar', bool())
print(str(c.speed) + ' ' + c.color+' ' + c.name+' ' + str(c.is_police))
c.go()
c.turn('back')
c.show_speed()
c.show_speed()
c.stop()

c = PoliceCar(80, 'blue', 'PoliceCar', bool(1))
print(str(c.speed) + ' ' + c.color+' ' + c.name+' ' + str(c.is_police))
c.go()
c.turn('up')
c.show_speed()
c.stop()