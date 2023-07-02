print('Qual o meu pagamento?')
nome = str(input('Digite o seu nome: '))
valor = float(input('Digite o valor por hora: '))
horas = float(input('Digite o valor de horas trabalhadas: '))
pagamento = valor * horas
print(f'O valor a ser recebido por {nome} é de R${pagamento:.2f}. Parabéns por seu esforço!')