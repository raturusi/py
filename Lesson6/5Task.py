class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print(f'{self.title}. Запуск отрисовки.')

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ручки.')
class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандаша.')
class Handle (Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркера.')

s = Stationery("Перо")
print(s.title)
s.draw()
s = Pen("Ручка")
print(s.title)
s.draw()
s = Pencil("Карандаш")
print(s.title)
s.draw()
s = Handle("Иаркер")
print(s.title)
s.draw()