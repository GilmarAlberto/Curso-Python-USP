'''
Receba um número inteiro na entrada e imprima

Buzz

se o número for divisível por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.
'''

num = int(input("Digite um número: "))

print("Buzz" if num % 5 == 0 else num)