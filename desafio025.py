'''
Escreva a função n_primos que recebe como argumento um número inteiro maior ou igual a 2 como parâmetro e devolve a quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).
'''

def n_primos(num):
    qtd_primos = 0

    for contador in range(2, num + 1):
        ehPrimo = True
        for i in range(2, int(contador**0.5) + 1):
            if contador % i == 0:
                ehPrimo = False
                break
        if ehPrimo:
            qtd_primos += 1

    return qtd_primos

num = int(input("Digite um número maior ou igual a 2: "))

if num < 2:
    print("Número deve ser maior ou igual a 2.")
else:
    print(f"A quantidade de primos é {n_primos(num)}")
