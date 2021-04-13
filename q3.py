def _multiply(matrix):
    """Multiplicação de uma matriz por si mesma."""
    return [[sum([x * y for x, y in zip(row, col)]) for col in zip(*matrix)] for row in matrix]


def _sum_matrix(a, b, typ):
    """Soma de matrizes."""

    sum_matrix = None
    if typ == 'sum':
        sum_matrix = [[a[i][j] + b[i][j] for j in range(len(b))] for i in range(len(b))]
    elif typ == 'sub':
        sum_matrix = [[a[i][j] - b[i][j] for j in range(len(b))] for i in range(len(b))]
    return sum_matrix


def q3(matrix):
    """Calcula as expressões pedidas com auxílio das funções."""

    # A ** 3
    matrix_2 = _multiply(matrix)
    matrix_3 = _multiply(matrix_2)

    # A ** 2 - 2 * A + I
    I = [[1, 0], [0, 1]]
    matrix_versus2 = [[elem * 2 for elem in row] for row in matrix]
    sub_matrix = _sum_matrix(matrix_2, matrix_versus2, 'sub')
    final_matrix = _sum_matrix(sub_matrix, I, 'sum')

    return matrix_3, final_matrix
