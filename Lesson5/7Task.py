import json

d, a = {}, {}
e = 0
cnt = 0
try:
    with open("text_7.txt", "r", encoding='UTf-8') as f_in:
        for line in f_in:
            s = line.split()
            e += (int(s[2]) - int(s[3])) if int(s[2]) > int(s[3]) else 0
            d.update({s[0]: int(s[2]) - int(s[3])})
            cnt += 1 if int(s[2]) > int(s[3]) else 0
    a.update({"average_profit": (e / cnt)})
    my_list = [d, a]
    print(my_list)
    with open("text_7.json", "w", encoding='UTf-8') as f_out:
        json.dump(my_list, f_out)
except IOError:
    print('Ошибка IO')
