'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço
da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens
mais longas.
'''
dist = int(input('Qual é a distância da viagem? '))
if dist<=200:
    preço = dist*0.5
else:
    preço = dist*0.45
print(f'\033[0;35mVocê está prestes a começar uma viagem de {dist} Km.')
print(f'E o preço da sua passagem será de R${preço:.2f}')
