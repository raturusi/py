from random import randint
my_list = sorted([randint(0, el) for el in range(10, 30)])
print(my_list)
print([el for el in my_list if my_list.count(el) == 1])