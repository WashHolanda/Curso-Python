'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e
o menor peso lidos.
'''
pesos = [0,0,0,0,0]
for i in range(0,5):
    pesos[i] = float(input(f'Peso da {i+1}ª pessoa: '))
print(f'O maior peso lido foi de {max(pesos)}Kg.')
print(f'O maior peso lido foi de {min(pesos)}Kg.')
