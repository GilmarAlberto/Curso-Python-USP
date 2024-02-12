"""
Como pedido na videoaula desta semana, escreva um programa que calcula as raízes de uma equação do segundo grau.

O programa deve receber os parâmetros a, b e c da equacao ax**2+bx+c, respectivamente, e imprimir o resultado na saída da seguinte maneira:

Quando não houver raízes reais imprima:

esta equação não possui raízes reais

Quando houver apenas uma raiz (ou seja, uma raiz com multiplicidade 2) imprima:

a raiz desta equação é X

ou

a raiz dupla desta equação é X

onde X é o valor da raiz dupla

Quando houver duas raízes reais imprima:

as raízes da equação são X e Y

onde X e Y são os valor das raízes.

Além disso, no caso de existirem 2 raízes reais distintas, elas devem ser impressas em ordem crescente. Exemplos:

as raízes da equação são 1.0 e 2.0

as raízes da equação são -2.0 e 0.0
"""

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if a == 0:
    print("Essa equação não é de segundo grau")
    exit()

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("esta equação não possui raízes reais")
elif delta == 0:
    x = -b / (2 * a)
    print(f"A raiz desta equacao é {x}")
else:
    x = (-b + delta ** 0.5) / (2 * a)
    y = (-b - delta ** 0.5) / (2 * a)

    if x == y:
        print(f"A raiz dupla da equação é {x}") 
    else: 
        print(f"As raízes da equação são {min(x,y)} e {max(x,y)}")
