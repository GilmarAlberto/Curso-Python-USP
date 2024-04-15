"""
    Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.
"""

larg = int(input("Digite a largura: "))
alt  = int(input("Digite a altura: "))

for i in range(alt):
    for j in range(larg):
        if i == 0 or i == alt-1 or j == 0 or j == larg -1:
            print("#", end="")
        else:
            print(" ", end="")
    print("")