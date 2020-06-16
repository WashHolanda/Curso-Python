'''
Faça um programa que leia nome e média de um aluno, guardando também a situação em um 
dicionário. No final, mostre o conteúdo da estrutura na tela.
'''
aluno = {}
aluno['Nome'] = str(input('Nome: ')).title()
aluno['Média'] = float(input('Média: '))
if aluno['Média'] >= 6:
    aluno['Situação'] = 'Aprovado'
elif aluno['Média'] >= 3:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print('-='*15)
for k,v in aluno.items():
    print(f'- {k} é igual a {v}')
