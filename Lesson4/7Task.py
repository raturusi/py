from random import randrange
from math import factorial
my_number = randrange(1, 10)
def my_fact(n):
    k = 1
    for el in range(1, n+1):
        k *= el
        yield k
p = 1
r = ""
for el in my_fact(my_number):
    r += (" * " if r != "" else "") + str(int(el / p))
    p = el
print(f'{my_number}! = {r} = {p} ')
print(f'factorial({my_number}) = {factorial(my_number)}')
