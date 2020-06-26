from random import randint
with open('text_5.txt', "w") as f_out:
    f_out.write(" ".join([str(randint(0, x)) for x in range(10, 20)]))
with open('text_5.txt', "r") as f_out:
    s = 0
    for n in f_out.readline().split():
        s +=int(n)
    print(s)