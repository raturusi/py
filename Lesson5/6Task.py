d={}
try:
     with open("text_6.txt", "r", encoding='UTf-8') as f_in:
        for line in f_in:
            d.update({line.split()[0]: sum(list(map(lambda s: int(s.replace('-', '0').replace('(пр)', '').replace('(лаб)', '').replace('(л)', '')), line.split()[1:4])))})
     print(d)
except IOError:
    print('Ошибка IO')