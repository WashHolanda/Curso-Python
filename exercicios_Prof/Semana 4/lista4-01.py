'''
1) Faça um programa que leia o nome e nota da P1 de vários
alunos guardando tudo em uma lista e no final mostre:
a. Quantas alunos foram cadastradas
b. O nome do aluno com maior nota
c. O nome da pessoa menor nota
d. O nota média da sala.
'''
from operator import itemgetter

op = ' '
p1 = []
aluno = {}
média = 0

while op != 'N':
    aluno['nome'] = str(input('Nome: ')).title()
    aluno['nota'] = float(input('Nota 1: '))
    média += aluno['nota']
    p1.append(aluno.copy())
    aluno.clear()
    op = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    
print('-='*30)
print(f'Foram cadastrados {len(p1)} alunos.')
print(f'O aluno com a maior nota foi de {max(p1,key=itemgetter("nota"))["nome"]}')
print(f'O aluno com a menor nota foi de {min(p1,key=itemgetter("nota"))["nome"]}')
print(f'A nota média da sala foi {(média/len(p1)):.2f}')
