"""
Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.
Digite o valor de n: 5
1
3
5
7
9
"""
i = 1
contador = 0

num = int(input("Digite um número inteiro: "))

while(contador < num):
    if(i % 2 != 0):
        print(i)
        contador += 1
    i += 1
