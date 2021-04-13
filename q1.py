def q1(matrix):
    """Verifica se existem elementos repetidos ao adicionar os elementos em um conjunto (que não admite repetições)."""
    aux = {elem for row in matrix for elem in row}
    return len(aux) < len(matrix) * len(matrix[0])
