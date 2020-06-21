'''
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade
em um arquivo de texto simples. O sistema só terá 2 opções: cadastrar uma nova pessoa e
listar todas as pessoas cadastradas.

b)Vamos ver como fazer acesso a arquivos usando o Python.
'''
from lib import menu
from lib import arquivo


arq = "pessoas.txt"
op = 0

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while op != 3:
    menu.cabeçalho('MENU PRINCIPAL')
    menu.listaOpções(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do Sistema'])
    op = menu.lerOpção('Sua Opção: ')
    if op == 1:
        arquivo.lerArquivo(arq)
    elif op == 2:
        pass
menu.cabeçalho('Saindo do Sistema... Até logo!')
