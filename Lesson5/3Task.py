try:
    salary = 20000
    with open("text_3.txt", "r", encoding='UTf-8') as f_in:
        content = f_in.readlines()
    filter_content = list(filter(lambda s: float(list(s.split())[1]) < salary, content))
    print(''.join(filter_content))
    sum_content = list(map(lambda s: float(list(s.split())[1]), content))
    print(f'{sum(sum_content)}/{len(sum_content)} = {sum(sum_content)/len(sum_content)}')
except IOError:
    print('Ошибка IO')