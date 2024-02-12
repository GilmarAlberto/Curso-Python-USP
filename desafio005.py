'''
Receba um número inteiro na entrada e imprima

 par 

quando o número for par ou

ímpar

quando o número for ímpar.
'''

num = int(input("Digite um número: "))

mensagem = "par" if num % 2 == 0 else "impar"

print(mensagem)