"""
Introdução à Ciência da Computação com Python Parte 2
Módulo 1 - Matrizes
Praticar tarefa de programação: Exercícios adicionais (opcionais)
https://www.coursera.org/learn/ciencia-computacao-python-conceitos-2/programming/KMUQc/exercicios-adicionais-opcionais

Exercício 1: Imprimindo matrizes

Como proposto na primeira vídeo-aula da semana, escreva uma função imprime_matriz(matriz), que recebe uma matriz como parâmetro e imprime a matriz, linha por linha. Note que NÃO se deve imprimir espaços após o último elemento de cada linha!

Dica: lembre da primeira parte do curso, na semana 7! A função "print" em geral adiciona uma quebra de linha ao final, mas você pode controlar isso usando o argumento opcional "end"

"""

import random

def cria_matriz(num_linhas, num_colunas):
    """
    (int, int) -> matriz (lista de listas)
    Cria e retorna uma matriz com num_linhas linhas e num_colunas colunas,
    preenchida com valores aleatórios entre 0 e 100.
    """

    matriz = [] #lista vazia

    for i in range(num_linhas):
        # cria a linha i
        linha = [] #lista vazia
        for j in range(num_colunas):
            linha.append(random.randint(0,100))

        #adiciona linha à matriz
        matriz.append(linha)

    return matriz

def imprime(matriz):
    for linha in matriz:
        # imprime cada linha com espaçamento fixo
        print(" ".join(f"{num:3}" for num in linha))


def main():

    lin = random.randint(1, 10)
    col = random.randint(1, 10)
           
    print(f"Criada uma matriz {lin}x{col}")

    matriz = cria_matriz(lin, col)

    imprime(matriz)
    
if __name__ == "__main__":
    main()