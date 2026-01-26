"""
Introdução à Ciência da Computação com Python Parte 2
Módulo 2 - Strings
https://www.coursera.org/learn/ciencia-computacao-python-conceitos-2/lecture/FTy4B/strings

Exercício – Nome mais curto

Escreva uma função chamada mais_curto que recebe uma lista de strings contendo nomes de pessoas e retorna o nome mais curto da lista, considerando o número de caracteres.

Regras:

Ignore espaços em branco antes e depois de cada nome.

O nome retornado deve estar capitalizado (apenas a primeira letra maiúscula).

Caso haja espaços extras nos nomes, eles não devem influenciar no cálculo do tamanho.

Em seguida, implemente uma função testa_mais_curto que realize testes automatizados para verificar se a função mais_curto funciona corretamente em diferentes cenários.

"""
def testa_mais_curto():
    # caso 1: nomes simples
    lista = ["ana", "jose", "maria"]
    assert mais_curto(lista) == "Ana"

    # caso 2: nomes com espaços antes e depois
    lista = ["   ana   ", "  jose", "maria   "]
    assert mais_curto(lista) == "Ana"

    # caso 3: nome mais curto no meio
    lista = ["alberto", "leo", "fernando"]
    assert mais_curto(lista) == "Leo"

    # caso 4: nome mais curto no final
    lista = ["cristina", "roberto", "ana"]
    assert mais_curto(lista) == "Ana"

    # caso 5: empate de tamanho (deve retornar o primeiro)
    lista = ["ana", "bia", "carla"]
    assert mais_curto(lista) == "Ana"

def mais_curto(lista):
    
    nome = lista[0].strip()

    for n in lista:

        n_limpo = n.strip()
        if len(n_limpo) < len(nome):
            nome = n_limpo

    return nome.capitalize()


def main():
    lista = ["Gilmar", "Alberto", "  de  ", "Abreu", "Pinto"]
    print(mais_curto(lista))

if __name__ == "__main__":
    testa_mais_curto()
    print("Todos os testes passaram!")
    main()
