"""
Introdução à Ciência da Computação com Python Parte 2
Módulo 2 - Strings

https://www.coursera.org/learn/ciencia-computacao-python-conceitos-2/programming/ab30i/exercicios-adicionais-opcionais

Exercício 1: Contando vogais ou consoantes

Escreva a função conta_letras(frase, contar="vogais"), que recebe como primeiro parâmetro uma string contendo uma frase e como segundo parâmetro uma outra string. Este segundo parâmetro deve ser opcional.

Quando o segundo parâmetro for definido como "vogais", a função deve devolver o numero de vogais presentes na frase. Quando ele for definido como "consoantes", a função deve devolver o número de consoantes presentes na frase. Se este parâmetro não for passado para a função, deve-se assumir o valor "vogais" para o parâmetro.
"""

def conta_letras(frase, contar="vogais"):

    vogais, consoantes = 0, 0

    for letra in frase:

        if letra.isalpha():
            if letra.lower() in "aeiou":
                vogais += 1
            else:
                consoantes += 1

    if contar == "vogais": 
        return vogais
    else: 
        return consoantes

def testa_conta_letras():
    print("Teste 1 – vogais em 'aeiou'")
    resultado = conta_letras("aeiou")
    print("Resultado:", resultado)
    assert resultado == 5

    print("Teste 2 – consoantes em 'bcdfg'")
    resultado = conta_letras("bcdfg", "consoantes")
    print("Resultado:", resultado)
    assert resultado == 5

    print("Teste 3 – vogais em 'Python'")
    resultado = conta_letras("Python")
    print("Resultado:", resultado)
    assert resultado == 1

    print("Teste 4 – consoantes em 'Python'")
    resultado = conta_letras("Python", "consoantes")
    print("Resultado:", resultado)
    assert resultado == 5

    print("Teste 5 – string vazia")
    resultado = conta_letras("")
    print("Resultado:", resultado)
    assert resultado == 0

    print("Teste 6 – caracteres não alfabéticos")
    resultado = conta_letras("123 !@#")
    print("Resultado:", resultado)
    assert resultado == 0

    print("Teste 7 – frase completa (vogais)")
    resultado = conta_letras("Gilmar Alberto de Abreu Pinto")
    print("Resultado:", resultado)
    assert resultado == 11

    print("Teste 8 – frase completa (consoantes)")
    resultado = conta_letras("Gilmar Alberto de Abreu Pinto", "consoantes")
    print("Resultado:", resultado)
    assert resultado == 14

    print("✔ Todos os testes individuais passaram!")

def main():

    frase = "Gilmar Alberto de Abreu Pinto"

    print(f"vogais: {conta_letras(frase)}")
    print(f"consoantes: {conta_letras(frase, 'consoantes')}")

if __name__ == "__main__":
    testa_conta_letras()
    print("Todos os testes passaram!")
    main()

