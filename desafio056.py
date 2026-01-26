"""
Introdução à Ciência da Computação com Python Parte 2
Módulo 2 - Strings

Escreva uma função em Python que receba como parâmetro uma lista de strings e retorne a string que aparece primeiro na ordem lexicográfica, ignorando diferenças entre letras maiúsculas e minúsculas.

⚠️ Atenção:

A string retornada não é necessariamente o primeiro elemento da lista.

A comparação deve considerar a ordem alfabética, isto é, palavras que começam com “a” vêm antes das que começam com “b”, e assim por diante.

A comparação deve ser feita sem diferenciar letras maiúsculas de minúsculas.

Você pode escolher o nome da função, por exemplo:
menor_string(lista)

Testes

Implemente também uma função de teste para verificar se a sua função está correta.

Essa função de teste deve:

Executar vários casos de teste;

Comparar o resultado retornado com o valor esperado;

Verificar o comportamento da função em diferentes cenários.

Exemplos de situações que devem ser testadas:

Palavras com letras maiúsculas e minúsculas misturadas;

Palavras fora de ordem na lista;

Listas com diferentes quantidades de strings.
"""

def testa_menor_string():
    assert menor_string(["ana", "maria", "José", "Valdemar"]) == "ana"
    assert menor_string(["Gilmar", "Alberto", "Abreu", "Pinto"]) == "Abreu"
    assert menor_string(["zebra", "Alfa", "beta"]) == "Alfa"
    assert menor_string(["Python"]) == "Python"


def menor_string(lista):

    menor = lista[0]

    for s in lista[1:]:
        if s.lower() < menor.lower():
            menor = s

    return menor

def main():
    lista = ["Gilmar", "Alberto", "  de  ", "Abreu", "Pinto"]
    print(menor_string(lista))

if __name__ == "__main__":
    testa_menor_string()
    print("Todos os testes passaram!")
    main()