'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com
idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá
também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos
anos a pessoa vai se aposentar.
'''
from datetime import date
pessoa = {}
pessoa['nome'] = str(input('Nome: ')).title()
nasc = int(input('Ano de Nascimento: '))
pessoa['idade'] = date.today().year - nasc
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não possui): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de Contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = (pessoa['contratação'] + 35) - nasc
print('-='*20)
for k,v in pessoa.items():
    print(f'    -{k} tem o valor {v}')
