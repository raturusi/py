class IsNumeric(Exception):
    def __init__(self, txt):
        self.txt = txt

my_digits=[]
while True:
    inp = input('Введите число или строку, для завершения ввода stop:')
    if inp == 'stop':
        break
    try:
        for i in inp:
            if not i in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                raise IsNumeric('Вы ввели не число')
        my_digits.append(int(inp))
    except IsNumeric as err:
        print(err)
print(my_digits)