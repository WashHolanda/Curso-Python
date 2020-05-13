'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e 
mostre quantos Dólares ela pode comprar.
Considere: US$1,00 = R$5,91
'''
reais = float(input('Quanto dinheiro você tem na carteira? R$'))
print(f'Com R${reais:.2f} você pode comprar U${reais/5.91:.2f}')
