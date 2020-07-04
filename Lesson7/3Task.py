from math import ceil

class Ceil:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        if self.num < other.num:
            print('Разность  д.б. > 0')
        return self.num - other.num if self.num > other.num else self.num

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        return round(self.num / other.num)

    def make_order(self, r):
        return '\n'.join('*'*r for i in range(self.num//r))+('\n' if self.num > r else '') + '*' * (self.num % r if r < self.num else self.num)

my_ceil1 =  Ceil(10)
my_ceil2 = Ceil(6)
print(f'Сумма: \n{Ceil(my_ceil1 + my_ceil2).make_order(10)}')
print()
print(f'Разность: \n{Ceil(my_ceil1 - my_ceil2).make_order(10)}')
print()
print(f'Умножение: \n{Ceil(my_ceil1 * my_ceil2).make_order(10)}')
print()
print(f'Деление: \n{Ceil(my_ceil1 / my_ceil2).make_order(10)}')