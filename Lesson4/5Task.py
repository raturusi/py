from functools  import reduce
my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(my_list)
def my_func(m1, m2):
    return m1*m2
print(reduce(my_func,my_list))