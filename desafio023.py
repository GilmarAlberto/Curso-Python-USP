"""
Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes à largura e à altura de um retângulo, respectivamente. O programa deve imprimir, usando repetições encaixadas (laços aninhados), uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída.
"""

larg = int(input("Digite a largura: "))
alt  = int(input("Digite a altura: "))

for i in range(alt):
    for j in range(larg):
        print("#", end="")
    print("")


