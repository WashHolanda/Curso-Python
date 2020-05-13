'''
Faça um programa que leia o preço de um produto e mostre seu novo preço com 5%
de desconto.
'''
preço = float(input('Qual o valor do produto? R$'))
print(f'O produto que custava R${preço:.2f}, na promoção com desconto de 5%', end='')
print(f' vai custar R${preço*(1-(5/100)):.2f}')
