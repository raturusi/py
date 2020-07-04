from abc import ABC, abstractmethod

class MyClothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_material_consumption(self):
        pass

class MyCoat(MyClothes):
    def __init__(self, name, v):
        self.v = v
        MyClothes.__init__(self, name)

    @property
    def v(self):
        return self.__v

    # сеттер для создания свойств
    @v.setter
    def v(self, v):
        if v < 45:
            self.__v = 50
        elif v > 60:
            self.__v = 50
        else:
            self.__v = v

    def get_material_consumption(self):
        return self.v/6.5 + 0.5

class MySuit(MyClothes):
    def __init__(self, name, h):
        self.h = h
        MyClothes.__init__(self, name)

    @property
    def h(self):
        return self.__h

    # сеттер для создания свойств
    @h.setter
    def h(self, h):
        if h < 120:
            self.__h = 170
        elif h > 200:
            self.__h = 170
        else:
            self.__h = h

    def get_material_consumption(self):
        return 2 * self.h + 0.3

mycoat = MyCoat('Пальто', 52)
print(f'{mycoat.name} - {mycoat.v} - {mycoat.get_material_consumption():.2f}')
mysuit = MySuit('Костюм', 175)
print(f'{mysuit.name} -  {mysuit.h} - {mysuit.get_material_consumption():.2f}')