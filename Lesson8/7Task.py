class Complex:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Complex(self.number + other.number)

    def __mul__(self, other):
        return Complex(self.number * other.number)


class MyComplex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return MyComplex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return MyComplex(self.a * other.a + self.b * other.b * -1, self.a * other.b + self.b * other.a)

    def __str__(self):
        return '('+str(self.a) + ('+' if self.b >= 0 else '') + str(self.b)+'i)'

    @classmethod
    def getmycomlex(cls, number):
        try:
            a, b = 0, 0
            if '+' in number:
                a, b = list(map(lambda n: int(n.lower().replace('j', '').replace('(', '').replace(')', '')), number.split('+')))
                return cls(a, b)
            elif '-' in number:
                a, b = list(map(lambda n: int(n.lower().replace('j', '').replace('(', '').replace(')', '')), number.split('-')))
                b *= -1
                return cls(a, b)
            else:
                print('Некорректный формат комплексного числа (a + ib), a b - действительные числа')
                return None
        except ValueError:
            print('Некорректный формат комплексного числа (a + ib), a b - действительные числа')
            return None


c1 = Complex(complex(2, -3))
c2 = Complex(complex(5, 8))
c = c1 + c2
print(f'{c1.number} + {c2.number} = {c.number}')
c = c1 * c2
print(f'{c1.number} * {c2.number} = {c.number}')
print('MyClass')
myc1 = MyComplex.getmycomlex(str(c1.number))
myc2 = MyComplex.getmycomlex(str(c2.number))
if myc1 is not None and myc2 is not None:
    print(f'{myc1} + {myc2} = {myc1 + myc2}')
    print(f'{myc1} * {myc2} = {myc1 * myc2}')
