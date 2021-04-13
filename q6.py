def q6(array):
    """
    Imprime uma matriz simétrica.

    :param array: a matriz simétrica. A lista de listas que representa a matriz não precisa ter sub-listas de
                    tamanho iguais, visto que, por ser simétrica, os elementos de índice `i != j` são equivalentes.
    :raise ValueError: se a matriz não possuir elementos.
    """
    size = len(array)
    if size == 0:
        raise ValueError("a matriz está vazia")

    matrix = []
    current_row = 0
    current_col = 0
    for value in array:
        if current_col == current_row:
            row = []
            matrix.append(row)

            current_row += 1
            current_col = 0
        else:
            row = matrix[-1]

        row.append(value)
        current_col += 1

    n = len(matrix[-1])
    for i in range(n):
        row = matrix[i]
        for j in range(i + 1, n):
            row.append(matrix[j][i])

    return matrix
