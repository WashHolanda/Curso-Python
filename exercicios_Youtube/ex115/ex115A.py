'''
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade
em um arquivo de texto simples. O sistema só terá 2 opções: cadastrar uma nova pessoa e
listar todas as pessoas cadastradas.

a)Vamos criar um menu em Python, usando modularização.
'''
from lib import menu

op = 0
while op != 3:
    menu.cabeçalho('MENU PRINCIPAL')
    menu.listaOpções(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do Sistema'])
    op = menu.lerOpção('Sua Opção: ')
    print('\033[m',menu.linha())
    print(f'{f"Opção {op}":^40}')
    print('\033[m',menu.linha())
print(f'{"Saindo do Sistema... Até logo!":^40}')
print(menu.linha())
