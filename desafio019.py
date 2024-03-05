"""
Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.
"""

def vogal(letra):

    if(letra.lower() in "aeiou"):
        return True
    else:
        return False   


letra = input("Digite uma letra: ")

print(vogal(letra))

