'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
pessoas ainda não atingiram a maioridade e quantas já são maiores.
''' 
from datetime import date
maior = 0
menor = 0
for i in range(0,7):
    ano = int(input(f'Em que ano a {i+1}ª pessoa nasceu? '))
    if (date.today().year - ano) >= 18:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'E também tivemos {menor} pessoas menores de idade')
