'''
Uma empresa de cartão de crédito envia suas faturas por email com a seguinte mensagem:

Olá, Fulano de Tal
A sua fatura com vencimento em 9 de Janeiro no valor de R$ 350,00 está fechada.

Escreva um programa que receba (entrada de dados através do teclado) o nome do cliente, o dia de vencimento, o mês de vencimento e o valor da fatura  e imprima (saída de dados) a mensagem com os dados recebidos, no mesmo formato da mensagem acima. Note que o programa imprime a saída em duas linhas diferentes. Note também que, como não é preciso realizar cálculos, o valor não precisa ser convertido para número, pode ser tratado como texto.
'''

cliente = input("Digite o nome do cliente: ")
diaVcto = input("Digite o dia de vencimento: ")
mesVcto = input("Digite o mês de vencimento: ") 
vlrFat  = float(input("Digite o valor da fatura: "))

print(f'Olá, {cliente}')
print(f'A sua fatura com vencimento em {diaVcto} de {mesVcto} no valor de {vlrFat:.2f} está fechada.')
