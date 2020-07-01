class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_weight(self, thick):
        return self._length * self._width * thick * 25 / 1000


try:
    r = Road(int(input('Введите длину дороги в метрах(м): ')), int(input('Введите ширину дороги(м): ')))
    t = int(input('Введите толщину асфальта(см): '))
    print(f'Вес асфальта (т) = {r._length} * {r._width} * {t} * 25 = {r.get_weight(t)}')
except ValueError:
    print("Введены некорректные данные!")
