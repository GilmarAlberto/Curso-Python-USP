'''
Introdução à Ciência da Computação com Python Parte 1
Módulo 8 listas

Exercício 2 - Soma dos elementos de uma lista

Escreva a função soma_elementos que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro correspondente à soma dos elementos da lista recebida.
'''

import random

def soma_elementos(lista):
    return sum(lista)

lista = [random.randint(1, 10) for _ in range(10)]
print(lista)

print(f'A soma é {soma_elementos(lista)}')
