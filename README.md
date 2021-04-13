# Paradigma imperativo

Tarefa 1 da disciplina de Paradigmas de Linguagens de Programação.

Os códigos-fonte para cada questão do PDF original estão distribuídos nos arquivos *q\*.py*,
onde também estão incluídas explicações sobre o funcionamento do algoritmo. Para executar as questões
e verificar suas saídas, foi criado um interpretador de comandos que pode ser acessado ao executar o arquivo
*main.py*.

## Integrantes

- Danilo Daniel Pojo Paraíso
- Enzo Gabriel da Rocha Santos
- Lucas Mesquita Rodrigues Ferreira

## Uso

Ao executar o arquivo *main.py* aparecerá a seguinte mensagem, que aguardará o usuário inserir um comando:

```
>
```

Para executar a questão *n*, basta digitar o comando `q[n]` com os seus argumentos necessários. Abaixo estão
alguns exemplos de comandos que podem ser inseridos no interpretador e suas respectivas saídas, que podem ser
verificadas na sua execução:

```
> q1 [[1, 2, 3], [4, 5, 6]]
False

> q1 [[1, 2, 3], [3, 2, 1]]
True

> q2 [[4, 1, 2, 3], [5, 2, 1, 400], [2, 1, 3, 8], [7, 1, 2, 5]], [0, 3, 1, 3, 3, 2, 1, 0]
417

> q3
{'A^2 - 2A + I': [[0, 0], [0, 0]], 'A^3': [[1, 0], [0, 1]]}

> q4 1
[[1.0, 0.5, 0.3333333333333333],
 [0.25, 1.0, 0.2],
 [0.16666666666666666, 0.14285714285714285, 1.0]]

> q4 2
[[1.1805555555555556, 1.0476190476190477, 0.7666666666666666],
 [0.5333333333333333, 1.1535714285714285, 0.48333333333333334],
 [0.36904761904761907, 0.369047619047619, 1.084126984126984]]

> q4 1712
[[1.6035126754673357e+308, inf, inf],
 [1.0999247339175564e+308, 1.4202398710278686e+308, 1.2648126764569272e+308],
 [8.249195581647713e+307, 1.0651489240754869e+308, 9.485819184262974e+307]]

> q5 [[0, -1, 0, -1, -1, 0, -1, 0], [0, 0, 0, 0, -1, 0, 0, 0], [0, 0, -1, -1, 0, 0, -1, 0], [-1, 0, 0, 0, 0, -1, 0, 0], [0, 0, -1, 0, 0, 0, -1, -1]]
[[1, -1, 2, -1, -1, 3, -1, 4],
 [5, 6, 0, 0, -1, 7, 0, 0],
 [8, 0, -1, -1, 9, 0, -1, 0],
 [-1, 10, 0, 11, 0, -1, 12, 0],
 [13, 0, -1, 14, 0, 0, -1, -1]]

> q6 ['a', 'b', 'f', 'c', 'g', 'j', 'd', 'h', 'm', 'l', 'e', 'i', 'n', 'o', 'k']
[['a', 'b', 'c', 'd', 'e'],
 ['b', 'f', 'g', 'h', 'i'],
 ['c', 'g', 'j', 'm', 'n'],
 ['d', 'h', 'm', 'l', 'o'],
 ['e', 'i', 'n', 'o', 'k']]

> q7 [[0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
True

> q7 [[2, -1, 0], [-1, 2, 0], [0, 0, 1]]
False
```

Ao inserir o comando `help q[n]`, onde *n* é o número de uma questão, o comando da respectiva questão será 
mostrado na tela. 

É importante notar que:

- Para executar a questão 4, é preciso instalar a biblioteca `numpy` pelo comando `python -m pip install numpy`.

- A questão 3 não possui entrada, visto que a matriz já foi disponibilizada no comando da questão.

- A questão 4 possui como entrada apenas o valor de *k*, visto que a matriz também foi disponibilizada no comando da questão.

- A questão 6 recebe como entrada um vetor com *n(n + 1) / 2* elementos como informado no comando da questão. 
Apesar de no exemplo acima o vetor possuir elementos do tipo `str`, seus valores também podem ser numéricos.
