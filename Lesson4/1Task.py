from sys  import argv
def getsalary(hours, rate, prize):
     return hours*rate+prize
try:
    prog, h, r, p = argv
    print(f'Зарплата работниа = {getsalary(float(h), float(r), float(p))}')
except ValueError:
    print('Ошибка в параметрах')
