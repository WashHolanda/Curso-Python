'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista 
composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário
possa mostrar as notas de cada aluno individualmente.
'''
op = ' '
listaAlunos = []
aluno = []
while op != 'N':
    aluno.append(str(input('Nome: ')).title())
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    aluno.append(((aluno[1]+aluno[2])/2))
    listaAlunos.append(aluno[:])
    aluno.clear()
    op = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
print('-='*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*22)
for num,aluno in enumerate(listaAlunos):
    print(f'{num:<4}{aluno[0]:<10}{aluno[3]:>8.2f}')
print('-'*22)
num = 0
while num >= 0:
    num = int(input('De qual aluno deseja ver as notas(-1 encerra o programa)? '))
    print(f'Notas de {listaAlunos[num][0]} são {listaAlunos[num][1]} e {listaAlunos[num][2]}')
    print('-'*60)
