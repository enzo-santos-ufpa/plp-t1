def q2(matrix, path) -> int:
    """
    Calcula o custo total para um conjunto de itinerários.

    :param matrix: os custos de transporte da cidade `i` para a cidade `j`, onde `i` e `j` são indíces da matriz.
    :param path: o itinerário a ser percorrido, onde seus valores são índices da matriz.
    :return: o custo total para cada itinerário.
    """
    return sum(matrix[i][j] for i, j in zip(path[:-1], path[1:]))
