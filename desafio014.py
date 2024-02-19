"""
Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída

Exemplo:

Digite um número inteiro: 123
6
"""

num = int(input("Digite um número inteiro: "))

# Inicializa a soma dos dígitos
soma_digitos = 0

# Enquanto o número for maior que zero, extraímos os dígitos e somamos
while num > 0:
    # Obtém o último dígito do número usando a operação de módulo
    digito = num % 10
    # Adiciona o último dígito à soma
    soma_digitos += digito
    # Remove o último dígito do número, dividindo-o por 10 e convertendo para inteiro
    num //= 10

# Imprime a soma dos dígitos
print("A soma dos dígitos do número é:", soma_digitos)

