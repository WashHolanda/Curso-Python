'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''
valor = int(input('Que valor você quer sacar? R$'))
notaValor = 50
notaQuant = 0
while 1:
    if valor >= notaValor:
        valor -= notaValor
        notaQuant += 1
    else:
        print(f'Total de {notaQuant} cédulas de R${notaValor},00')
        if notaValor == 50:
            notaValor = 20
        elif notaValor == 20:
            notaValor = 10
        elif notaValor == 10:
            notaValor = 1
        notaQuant = 0
        if valor == 0:
            break
