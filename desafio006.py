'''
Receba um número inteiro na entrada e imprima 

Fizz

 se o número for divisível por 3. Caso contrário, imprima o mesmo número que foi dado na entrada.
'''

num = int(input("Digite um número: "))

print("Fizz" if num % 3 == 0 else num)