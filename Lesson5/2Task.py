try:
    wcount, scount = 0, 0
    with open("newtextfile.txt") as f_in:
        for line in f_in:
            scount += 1
            wcount += len(line.split())
    print(f'Строк в файле - {scount}, слов в файле - {wcount}')
except IOError:
    print('Ошибка IO')


