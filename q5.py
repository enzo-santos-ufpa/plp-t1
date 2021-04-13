import copy


def q5(matrix):
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    new_matrix = copy.deepcopy(matrix)

    word_count = 0
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == -1:
                new_matrix[i][j] = value
                continue

            # Verifica se a palavra começa em uma margem horizontal
            is_starting_col = i == 0 or matrix[i - 1][j] == -1

            # Verifica se a palavra começa em uma margem vertical
            is_starting_row = j == 0 or matrix[i][j - 1] == -1

            # Armazena se uma palavra foi encontrada
            has_found_word = False

            if is_starting_row:
                j_ = j + 1
                while j_ <= n_cols - 1 and matrix[i][j_] != -1:
                    j_ += 1
                    if j_ - j >= 2:
                        has_found_word = True
                        break

            if not has_found_word and is_starting_col:
                i_ = i + 1
                while i_ <= n_rows - 1 and matrix[i_][j] != -1:
                    i_ += 1
                    if (i_ - i) >= 2:
                        has_found_word = True
                        break

            if has_found_word:
                word_count += 1
                new_matrix[i][j] = word_count
            else:
                new_matrix[i][j] = value

    return new_matrix
