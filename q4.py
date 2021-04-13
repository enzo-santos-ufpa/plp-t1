import numpy as np


def q4(A, K):
    return np.linalg.matrix_power(A, K).tolist()
    # À medida que K tende ao infinito, os números da matriz também tendem. Por exemplo,
    # Se o K for igual a 1712 aqui, dois dos 9 números já são representados como sendo
    # infinitos.
