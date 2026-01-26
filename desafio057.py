"""
Introdução à Ciência da Computação com Python Parte 2
Módulo 2 - Strings

https://www.coursera.org/learn/ciencia-computacao-python-conceitos-2/programming/EF3RS/lista-de-exercicios-2
Exercício 1: Letras maiúsculas

Escreva a função maiusculas(frase) que recebe uma frase (uma string) como
parâmetro e devolve uma string com as letras maiúsculas que existem nesta
frase, na ordem em que elas aparecem.

Para resolver este exercício, pode ser útil verificar a tabela ASCII,
que contém os valores de cada caractere.

https://pt.wikipedia.org/wiki/ASCII

Note que, para simplificar a solução do exercício, as frases passadas
para a função não possuirão caracteres que não estejam presentes na
tabela ASCII apresentada, como ç, á, É, ã, etc.

Dica: Os valores apresentados na tabela são os mesmos devolvidos pela
função ord().
"""


def maiusculas(frase):
    """
    Recebe uma string e retorna outra string contendo apenas
    as letras maiúsculas (A–Z) presentes na frase, na ordem
    em que aparecem.
    """
    resultado = ""

    for c in frase:
        if 65 <= ord(c) <= 90:
            resultado += c

    return resultado


def main():
    """
    Função principal para executar os testes automatizados.
    """
    assert maiusculas("Bom Dia!") == "BD"
    assert maiusculas("Python") == "P"
    assert maiusculas("python") == ""
    assert maiusculas("ABCdefG") == "ABCG"
    assert maiusculas("") == ""
    assert maiusculas("123!@#") == ""

    print("Todos os testes passaram com sucesso!")


if __name__ == "__main__":
    main()
