'''
Introdução à Ciência da Computação com Python Parte 2
Módulo 1 - Matrizes
Tarefa de programação: Lista de exercícios - 1

https://www.coursera.org/learn/ciencia-computacao-python-conceitos-2/programming/ZP9BZ/lista-de-exercicios-1

Exercício 2: Soma de matrizes

Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes e devolve uma matriz que represente sua soma caso as matrizes tenham dimensões iguais. Caso contrário, a função deve devolver False.
'''

def soma_matrizes(m1, m2):

    # verifica número de linhas
    if len(m1) != len(m2):
        return False

    # verifica número de colunas
    for i in range(len(m1)):
        if len(m1[i]) != len(m2[i]):
            return False

    soma = []

    for i in range(len(m1)):
        linha = []
        for j in range(len(m1[i])):
            linha.append(m1[i][j] + m2[i][j])
        soma.append(linha)

    return soma

def main():
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    
    print(soma_matrizes(m1, m2))


if __name__ == "__main__":
    main()