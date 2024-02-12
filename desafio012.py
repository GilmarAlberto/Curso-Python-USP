"""
Escreva um programa que receba um número natural n na entrada e imprima n! (fatorial) na saída.
"""
n = int(input("Digite um número: "))

if(n==0):
    print("O fatorial de 0 é 1!")
else:
    fat = 1
    while(n >= 1):
        fat *= n
        n -= 1

    print(fat)

    