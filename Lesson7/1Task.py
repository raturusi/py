my_list = [[1, 2, 3], [3, 2, 1], [4, 5, 6], [6, 5, 4]]
print(my_list)
class Matrix:
    def __init__(self, mx):
        self.mx = mx

    def __str__(self):
        return '\n'.join(' '.join(map(str, s)) for s in self.mx)

    def __add__(self, other):
        my_sumlist = []
        for row in range(len(self.mx)):
            l = []
            for col in range(len(self.mx[0])):
                l.append(self.mx[row][col] + other.mx[row][col])
            my_sumlist.append(l)
        return Matrix(my_sumlist)

print(Matrix(my_list) + Matrix(my_list))
