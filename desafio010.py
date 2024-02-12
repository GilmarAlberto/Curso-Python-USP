"""
Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente, às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.

Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima

longe

na saída. Caso o contrário, quando a distância for menor que 10, imprima

perto


Dica: lembre-se que a fórmula da distância para dois pontos num plano cartesiano é a seguinte:

math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
"""

import math

x1 = int(input("Digite o x da coordenada 1: "))
y1 = int(input("Digite o y da coordenada 1: "))
x2 = int(input("Digite o x da coordenada 2: "))
y2 = int(input("Digite o y da coordenada 2: "))

distância = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("perto" if distância < 10 else "longe")