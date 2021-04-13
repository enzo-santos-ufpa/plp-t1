def q7(matrix):
    """Verifica se uma matriz é uma matriz de permutação, ao varrer a matriz na horizontal e diagonal"""
    for row in matrix:
        non_null = 0
        for elem in row:
            if elem == 1:
                non_null += 1
        if non_null != 1:
            return False

    for col in zip(*matrix):
        non_null = 0
        for elem in col:
            if elem == 1:
                non_null += 1
        if non_null > 1:
            return False

    return True
