"""
Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função
"""

def maior_primo(num):
    for i in range(num, 1, -1):
        primo = True
        for j in range(2, i//2 + 1):
            if i % j == 0:
                primo = False
                break
        if primo:
            return i

    return None

def main():
    while True:
        num = int(input("Digite um número maior ou igual a 2: "))

        if num >= 2:
            break

    print(f"O maior primo é {maior_primo(num)}")

if __name__ == '__main__':
    main()
