import random

def cria_matriz(num_linhas, num_colunas):
    """
    (int, int) -> matriz (lista de listas)
    Cria e retorna uma matriz com num_linhas linhas e num_colunas colunas,
    preenchida com valores aleatórios entre 0 e 100.
    """

    matriz = [] #lista vazia

    for i in range(num_linhas):
        # cria a linha i
        linha = [] #lista vazia
        for j in range(num_colunas):
            linha.append(random.randint(0,100))

        #adiciona linha à matriz
        matriz.append(linha)

    return matriz

def imprime(matriz):
    for linha in matriz:
        # imprime cada linha com espaçamento fixo
        print(" ".join(f"{num:3}" for num in linha))


def main():

    # lin = int(input("Digite o número de linhas: "))
    # col = int(input("Digite o número de colunas: "))

    lin = random.randint(1, 10)
    col = random.randint(1, 10)
           
    print(f"Criada uma matriz {lin}x{col}")

    # matriz = cria_matriz(lin, col, 0)
    matriz = cria_matriz(lin, col)

    imprime(matriz)
    
if __name__ == "__main__":
    main()