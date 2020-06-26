try:
    out_f = open("newtextfile.txt", "w")
    while True:
        s = input("Что записать в файл ? ")
        if not s:
            break
        else:
            out_f.write(s+'\n')

except IOError:
    print('Ошибка IO')
finally:
    out_f.close()
