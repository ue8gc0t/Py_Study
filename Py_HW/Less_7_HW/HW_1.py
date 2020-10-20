# Я понимаю, что код вполне рабочий, и вроде бы даже правильный, но мне очень интересно узнать, может
# есть какой-то более элегантный метод это сделать, потому что на мой взгляд больно массивно, а решения
# лучше в голову не приходит

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        string = ''
        for strings in self.matrix:
            for el in strings:
                string += str(el) + ' '
            string += '\n'
        return string

    def __add__(self, other):
        new_matrix = []
        if self.matrix_cmptblt(other.matrix):
            for i in range(0, len(other.matrix)):
                new_matrix.append([self.matrix[i][j] + other.matrix[i][j] for j in range(0, len(other.matrix))])
        return new_matrix

    def matrix_cmptblt(self, matrix):
        if len(self.matrix) == len(matrix):
            for el in zip(self.matrix, matrix):
                if len(el[0]) != len(el[1]):
                    return False
            return True
        else:
            return False


matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
matrix3 = Matrix(matrix1 + matrix2)

print(matrix1)
print(matrix3)
