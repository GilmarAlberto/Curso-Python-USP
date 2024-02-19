"""
Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".

Exemplos:

Digite um número inteiro: 13
primo

Digite um número inteiro: 12
não primo
"""

num = int(input("Digite um número inteiro: "))

i = num - 1

primo = True if num > 1 else False

while(i >= 2):
    if(num % i == 0):
        primo = False
        break
    i -= 1

print("primo" if primo else "não primo")