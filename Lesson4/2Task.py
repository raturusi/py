from random import randint
my_list = [randint(0, el) for el in range(90, 100)]
print(my_list)
print([my_list[el] for el in range(len(my_list)) if el > 0 and my_list[el] > my_list[el-1]])