'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com
a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar
ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo
que falta ou que passou do prazo.
'''
from datetime import date
ano = int(input('Ano de Nascimento: '))
idade = date.today().year-ano
print(f'Quem nasceu em {ano} tem {idade} anos em {date.today().year}.')
if idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o alistamento.')
    print(f'Seu alistamento será em {date.today().year + (18 - idade)}.')
elif idade == 18:
    print('Você tem que se alistar ainda esse ano!')
else:
    print(f'Você já deveria ter se alistado há {idade - 18} anos.')
    print(f'Seu alistamento foi em {date.today().year - (idade - 18)}.')
