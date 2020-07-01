class Worker:
    my_bonus={'Оклад1': {"wage": 100, "bonus": 50}, 'Оклад2': {"wage": 150, "bonus": 75}}
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname+', '+self.position
    def get_total_income(self):
        return Worker.my_bonus.get(self._income).get("wage") + Worker.my_bonus.get(self._income).get("bonus")
try:
    p = Position(input("Имя: "), input('Фамилия: '), input('Должность: '), input('Оклад(Оклад1, Оклад2): '))
    print(p.name+' '+p.surname+' '+p.position+' '+p._income)
    print(f'{p.get_full_name()} - {p.get_total_income()} руб.')
except AttributeError:
    print("Введены некорректные данные")

