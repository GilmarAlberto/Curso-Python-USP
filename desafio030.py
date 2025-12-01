'''
Introdução à Ciência da Computação com Python Parte 1
Módulo 8 listas

Exercício 2 - Invertendo sequência

Como pedido na primeira video-aula desta semana, escreva um programa que recebe uma sequência de números inteiros e imprima todos os valores em ordem inversa. A sequência sempre termina pelo número 0. Note que 0 (ZERO) não deve fazer parte da sequência.
'''

lista = []

while True:
    numero = int(input("Digite um número (0 para terminar): "))
    if numero == 0:
        break
    lista.append(numero)

# imprime a lista invertida
for valor in reversed(lista):
    print(valor)


