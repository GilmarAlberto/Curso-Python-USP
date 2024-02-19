"""
Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não".

Exemplo:

Digite um número inteiro: 12345
não

  um número inteiro: 1011
sim
"""

num = input("Digite um número: ")

ant = ""
msg = "não"

for i in(num):
    if(i == ant):
        msg = "sim"
        break
    ant = i

print(msg)