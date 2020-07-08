from random import randint

class MyZeroDivisionErr(Exception):
    def __init__(self, txt):
        self.txt = txt

try:
    for i in range(5, 10):
        d = randint(i, 10)
        d1 = randint(0, i)
        if d1 == 0:
            raise MyZeroDivisionErr(f"Делить на {d1} нельзя")
        print(f'{d}/{d1} = {d/d1}')
except MyZeroDivisionErr as err:
    print(err)



