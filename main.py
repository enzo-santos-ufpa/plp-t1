import ast
import cmd
import pprint


class ShellError(Exception):
    def __init__(self, prefix, message):
        self.prefix = prefix
        self.message = message

    def __str__(self):
        return f"[{self.prefix}] {self.message}"


class ExpectedError(ShellError):
    def __init__(self, message):
        super().__init__("ERRO", message)


class UnexpectedError(ShellError):
    def __init__(self, exception):
        super().__init__("ERRO INESPERADO", f"{exception}".capitalize())


class ParsingError(ExpectedError):
    pass


class ArgumentError(ExpectedError):
    pass


# noinspection PyArgumentList,PyCallingNonCallable,PyTypeChecker,PyMethodParameters
class QuestionShell(cmd.Cmd):
    prompt = '> '

    def __init__(self):
        super().__init__()
        from q1 import q1
        from q2 import q2
        from q3 import q3
        from q4 import q4
        from q5 import q5
        from q6 import q6
        from q7 import q7
        self._qs = (q1, q2, q3, q4, q5, q6, q7)

    def _check_input(method):
        from functools import wraps

        @wraps(method)
        def wrapper(self, *args, **kwargs):
            try:
                result = method(self, *args, **kwargs)
            except ShellError as e:
                print(e)
                return
            except Exception as e:
                print(UnexpectedError(e))
                return

            return result

        return wrapper

    @staticmethod
    def _check_args(line, expected_num_args):
        _receives_n_args = {
            0: "não recebe nenhum argumento",
            1: "recebe apenas um argumento"
        }.get(expected_num_args, f"recebe {expected_num_args} argumentos")

        value = QuestionShell._parse_object(line)

        if value is None:
            if expected_num_args > 0:
                raise ArgumentError(f"Essa questão {_receives_n_args}, porém não recebeu nenhum.")

            return value

        if isinstance(value, tuple):
            actual_num_args = len(value)
            if actual_num_args == expected_num_args:
                return value

            _received_n_args = None
            if actual_num_args < expected_num_args:
                _received_n_args = "não recebeu nenhum" if actual_num_args == 0 else f"recebeu apenas {actual_num_args}"

            elif actual_num_args > expected_num_args:
                _received_n_args = "não recebeu nenhum" if actual_num_args == 0 else f"recebeu {actual_num_args}"

            raise ArgumentError(f"Essa questão {_receives_n_args}, porém {_received_n_args}.")

        elif expected_num_args == 1:
            return value,

        raise ArgumentError(f"Essa questão {_receives_n_args}, porém recebeu 1.")

    @staticmethod
    def _parse_object(line: str):
        if not line:
            return None

        if line == 'inf':
            return float('inf')

        if line == 'nan':
            return float('nan')

        try:
            value = ast.literal_eval(line)
        except SyntaxError:
            raise ParsingError("O valor dado como entrada é inválido.")
        except ValueError:
            raise ParsingError("O valor dado como entrada é desconhecido.")

        return value

    @staticmethod
    def _parse_vector(obj: object, /, check_numeric=False):
        if not isinstance(obj, list):
            raise ParsingError("O valor dado como entrada não é um vetor.")

        if check_numeric and not all(isinstance(value, (float, int)) for value in obj):
            raise ParsingError("O vetor dado como entrada é invalido: alguns dos seus elementos não são numéricos.")
        return obj

    @staticmethod
    def _parse_matrix(obj: object, /, assure_square: bool = False):
        if not isinstance(obj, list):
            raise ParsingError("O valor dado como entrada não é uma matriz.")

        n_rows = len(obj)
        if n_rows == 0:
            raise ParsingError("A matriz dada como entrada possui não possui dimensão.")

        if any(not isinstance(row, list) for row in obj):
            raise ParsingError("A matriz dada como entrada é inválida: alguns de seus elementos não são listas.")

        cols_length = {len(row) for row in obj}
        if len(cols_length) > 1:
            raise ParsingError(
                "A matriz dada como entrada é inválida: algumas de suas linhas possuem tamanhos diferentes.")

        n_cols = cols_length.pop()
        if assure_square and n_cols != n_rows:
            raise ParsingError("A matriz dada como entrada não é quadrada.")

        return obj

    @_check_input
    def do_q1(self, line):
        """
        Dada uma matriz real A_mn, verificar se existem elementos repetidos em A.
        """
        obj, = self._check_args(line, 1)
        matrix = self._parse_matrix(obj)
        if matrix is None:
            return

        result = self._qs[0](matrix)
        print(result)

    @_check_input
    def do_q2(self, line):
        """
        Os elementos a_ij de uma matriz inteira A_nn representam os custos de transporte da cidade i para a cidade j.
        Dados n itinerários, cada um com k cidades, calcular o custo total cada itinerário.
        """
        objs = self._check_args(line, 2)
        matrix = self._parse_matrix(objs[0], assure_square=True)
        vector = self._parse_vector(objs[1])
        result = self._qs[1](matrix, vector)
        print(result)

    @_check_input
    def do_q3(self, line):
        """
        Seja A a matriz [[1, 0], [0, 1]]. Faça um programa em C, Python ou Java para calcular A^3 e A^2 - 2A + I, onde I
        é a matriz identidade.
        """
        _ = self._check_args(line, 0)
        m1, m2 = self._qs[2]([[1, 0], [0, 1]])
        pprint.pprint({"A^3": m1, "A^2 - 2A + I": m2})

    @_check_input
    def do_q4(self, line):
        """
        Seja A a matriz [[1, 1/2, 1/3], [1/4, 1, 1/5], [1/6, 1/7, 1]]. Faça um programa em C, Python ou Java onde você
        consiga descrever o que acontece com a matriz A^K quando é permitido a K crescer indefinidamente (ou seja,
        quando K tende ao infinito).
        """
        k, = self._check_args(line, 1)
        m = self._qs[3]([[1, 1 / 2, 1 / 3], [1 / 4, 1, 1 / 5], [1 / 6, 1 / 7, 1]], k)
        pprint.pprint(m)

    @_check_input
    def do_q5(self, line):
        """
        Em um jogo de palavra cruzada representada por uma matriz A_mn, onde cada elemento A_ij da matriz corresponde a
        uma letra (quadrado) do jogo, com 0 indicando um quadrado branco e -1 indicando um quadrado preto, pede-se fazer
        indicações na matriz das posições que são o início de palavras horizontais e/ou verticais nos quadrados
        correspondentes (nesse caso deve-se substituir os zeros), considerando que uma palavra deve ter pelo menos duas
        letras. Assim sendo, numere consecutivamente tais posições.
        """
        obj, = self._check_args(line, 1)
        matrix = self._parse_matrix(obj)
        if matrix is None:
            return

        result = self._qs[4](matrix)
        pprint.pprint(result)

    @_check_input
    def do_q6(self, line):
        """
        Uma matriz simétrica é uma matriz quadrada M_nn, onde não há necessidade, no caso de i ≠ j, de armazenar os
        elementos M_ij e M_ji, porque os dois tem o mesmo valor. Portanto basta guardar os elementos da diagonal
        principal e de metade dos elementos restante, por exemplo, os elementos abaixo da diagonal principal, para os
        quais i > j. Com isso tem-se uma economia de espaço usado para alocar a matriz, em vez de n^2 valores,
        armazena-se apenas S elementos. Pode-se determinar S como sendo a soma de uma PA (progressão aritmética), pois
        tem-se de armazenar um elemento da primeira linha, dois elementos da segunda, três da terceira e assim por
        diante (S = 1 + 2 + ... + n == n(n+1)/2).

        a) Implementar uma função para entrada dos elementos da matriz , considerando que não há necessidade, no caso de
        i ≠ j, de armazenar os elementos M_ij e M_ji, pois os mesmos tem o mesmo valor. Deve-se guardar somente os
        elementos da diagonal principal e dos elementos abaixo da diagonal principal, para os quais i>j.

        b) Implementar uma função para imprimir os elementos da matriz simétrica.
        """
        obj, = self._check_args(line, 1)
        vector = self._parse_vector(obj)
        if vector is None:
            return

        result = self._qs[5](vector)
        pprint.pprint(result)

    @_check_input
    def do_q7(self, line):
        """
        Dizemos que uma matriz inteira A_nn é uma matriz de permutação se em cada linha e em cada coluna houver n-1
        elementos nulos e um único elemento igual a 1. Implementar um código em C, Python ou Java que leia uma matriz
        A_mn e classifique aquela matriz como de permutação ou não.
        """
        obj, = self._check_args(line, 1)
        matrix = self._parse_matrix(obj, assure_square=True)
        if matrix is None:
            return

        result = self._qs[6](matrix)
        pprint.pprint(result)


def main():
    shell = QuestionShell()
    shell.cmdloop()


if __name__ == '__main__':
    main()
