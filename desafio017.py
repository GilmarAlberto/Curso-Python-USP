"""
Escreva a função maximo que recebe 2 números inteiros como parâmetro e devolve o maior deles.
"""

def maximo(n1, n2):
    return n1 if n1 > n2 else n2

def main():

    num1 = 10
    num2 = 50

    print(f"O maior número entre {num1} e {num2} é {maximo(num1,num2)}")

if __name__ == '__main__':
    main()