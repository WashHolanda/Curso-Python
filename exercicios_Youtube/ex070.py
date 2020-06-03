'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. 
'''
quant = total = 0
nome = input('Nome do produto: ')
nomeBarato = nome
preço = float(input('Preço: R$'))
preçoBarato = preço
while 1:
    total += preço
    if preço > 1000:
        quant += 1
    if preço < preçoBarato:
        nomeBarato = nome
        preçoBarato = preço
    op = ' '
    while op not in 'SN':
        op = input('Quer continuar [S/N]? ').strip().upper()
    if op == 'N':
        break
    nome = input('Nome do produto: ')
    preço = float(input('Preço: R$'))
print(f'O total da compra foi de R${total:.2f}.')
print(f'Temos {quant} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeBarato} que custa R${preçoBarato:.2f}')
