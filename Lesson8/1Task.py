class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def get_dmy(cls, date):
        try:
            day, month, year = cls(date).date.split('-')
            day = int(day)
            month = int(month)
            year = int(year)
            print(f'День {day} Месяц {month} Год {year}')
            return day, month, year
        except ValueError:
            print(f'Ошибка в дате {date}')
            return 0, 0, 0
        except TypeError:
            print('Введите дату в формате «день-месяц-год»')
            return 0, 0, 0
    @staticmethod
    def validatedmy(day, month, year):
        try:
            if not (1 <= day <= 31):
                print(f'День {day}  д.б. 1 <= day <=31')
            else:
                print(f'День {day} корректный');
            if not (1 <= month <= 12):
                print(f'Месяц {month} д.б. 1 <= month <=12')
            else:
                print(f'Месяц {month} корректный')
            if not (1900 <= year <= 2020):
                print(f'Год {year} д.б. 1900 <= year <= 2020')
            else:
                print(f'Год {year} корректный')
        except ValueError:
            print(f'Ошибка в {day} {month} {year}')
        except TypeError:
            print('Введите дату в формате «день-месяц-год»')
d, m, y = Date.get_dmy(input('Введите дату в формате «день-месяц-год»: '))
if d == 0 and m == 0 and y == 0:
    print('Введите дату в формате «день-месяц-год»')
else:
    Date.validatedmy(d, m, y)

mydate = Date(input('Введите дату в формате «день-месяц-год»: '))
d, m, y = mydate.get_dmy(mydate.date)
if d == 0 and m == 0 and y == 0:
    print('Введите дату в формате «день-месяц-год»')
else:
    mydate.validatedmy(d, m, y)
