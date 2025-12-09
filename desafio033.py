'''
Introdução à Ciência da Computação com Python Parte 2
Módulo 1 - Matrizes
Tarefa de programação: Lista de exercícios - 1

https://www.coursera.org/learn/ciencia-computacao-python-conceitos-2/programming/ZP9BZ/lista-de-exercicios-1

Exercício 1: Tamanho da matriz

Escreva uma função dimensoes(matriz) que recebe uma matriz como parâmetro e imprime as dimensões da matriz recebida, no formato iXj.

Observação: fazer tudo utilizando random.
'''

import random

def dimensoes(matriz):
    
    lin = len(matriz)
    col = len(matriz[0])
    print(f"{lin}x{col}")

def main():
    
    lin = random.randint(1, 10)
    col = random.randint(1, 10)

    matriz = [] #lista vazia

    matriz = [[random.randint(0, 100) for _ in range(col)] for _ in range(lin)]

    for linha in matriz:
        print(linha)

    dimensoes(matriz)

if __name__ == "__main__":
    main()