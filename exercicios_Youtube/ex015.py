'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro
alugado e a quantidade de dias pelo qual o carro foi alugado. Calcule o preço 
a pagar sabendo que o carro custa 60 reais por dia e 15 centavos por Km rodado.
'''
dias = int(input('Digite a quantidade de dias alugado: '))
km = float(input('Digite os KMs percorridos: '))
preco = (dias*60)+(km*0.15)
print(f'O valor a ser pago pelo aluguel é de R${preco:.2f}')
