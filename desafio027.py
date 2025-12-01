'''
Introdução à Ciência da Computação com Python Parte 1
Módulo 8 listas
Tarefa de programação: Lista de exercícios - 6

Exercício 1 - Removendo elementos repetidos

Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, verifica se tal lista possui elementos repetidos e os remove. A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.

Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?
'''

import random

def remove_repetidos(lista):
    return(sorted(set(lista)))

lista = [random.randint(1, 10) for _ in range(10)]
print(lista)

sem_repetidos = remove_repetidos(lista)

print(sem_repetidos)


