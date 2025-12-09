'''
Introdução à Ciência da Computação com Python Parte 1
Módulo 8 listas

Exercício 1 - Maior elemento de uma lista

Escreva a função maior_elemento que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro correspondente ao maior valor presente na lista recebida.
'''

import random

def maior_elemento(lista):
    return max(lista)
lista = [random.randint(1, 100) for _ in range(10)]
print(lista)


print(f'O maior número é {maior_elemento(lista)}')