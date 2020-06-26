try:
    my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    with open("text_4.txt") as f_in:
        content = f_in.readlines()
    translate_content = map(lambda s: s.replace(list(s.split())[0], my_dict.get(list(s.split())[0])), content)
    with open('translate.txt', "w", encoding='UTf-8') as f_out:
        for line in list(translate_content):
            f_out.write(line)
            print(line, end='')
except IOError:
    print('Ошибка IO')
