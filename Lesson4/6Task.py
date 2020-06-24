from itertools import count, cycle
from sys import argv


def my_range(st, en):
    my_list = []
    for i in count(st):
        if i > en - 1:
            break
        else:
            my_list.append(i)
    return tuple(my_list)


def my_cycle(st, en, it):
    my_list = []
    it *= (en-st)
    for j in cycle((str(el) for el in my_range(st, en))):
        if (en-st)*it < en - st:
            break
        else:
            my_list.append(j)
            it -= 1
    return tuple(my_list)


try:
    p, s, e, i = argv
    s, e, i = int(s), int(e), int(i)
    print(f'my_range = {my_range(s, e)}')
    print('my_range = ', end="")
    for el in my_range(s, e):
        print(el, end=" ")
    print('\n')
    print(f'my_cycle = {my_cycle(s, e, i)}')
    print('my_cycle = ', end="")
    for el in my_cycle(s, e, i):
        print(el, end=" ")
except ValueError:
    print('Ошибка параметров')
