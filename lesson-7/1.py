class Matrix:

    def __init__(self, my_matrix):
        self.my_matrix = my_matrix

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.my_matrix)

    def __add__(self, other):
        for i in range(len(self.my_matrix)):
            for j in range(len(other.my_matrix[i])):
                self.my_matrix[i][j] = self.my_matrix[i][j] + other.my_matrix[i][j]
        return Matrix.__str__(self)

mat_1 = Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 1], [1, 0, 0]])
mat_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3]])
print(mat_1.__add__(mat_2))
