"""
Introdução à Ciência da Computação com Python Parte 2
Módulo 1 - Matrizes
Praticar tarefa de programação: Exercícios adicionais (opcionais)
https://www.coursera.org/learn/ciencia-computacao-python-conceitos-2/programming/KMUQc/exercicios-adicionais-opcionais

Exercício 2: Matrizes multiplicáveis

Duas matrizes são multiplicáveis se o número de colunas da primeira é igual ao número de linhas da segunda. Escreva a função sao_multiplicaveis(m1, m2) que recebe duas matrizes como parâmetro e devolve True se as matrizes forem multiplicavéis (na ordem dada) e False caso contrário.

"""

def sao_multiplicaveis(m1, m2):
    """
    Retorna True se as matrizes m1 e m2 forem multiplicáveis
    (na ordem m1 x m2) e False caso contrário.
    """
    return len(m1[0]) == len(m2)


def main():
    # Caso 1: multiplicáveis
    m1 = [[1], [2], [3]]
    m2 = [[1, 2, 3]]
    print(sao_multiplicaveis(m1, m2))  # True

    # Caso 2: não multiplicáveis
    m3 = [[1, 2, 3], [4, 5, 6]]
    m4 = [[1, 2], [3, 4], [5, 6], [7, 8]]
    print(sao_multiplicaveis(m3, m4))  # False


if __name__ == "__main__":
    main()
