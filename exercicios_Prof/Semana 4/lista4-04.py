'''
4) Faça um programa que leia o nome RA e média final de uma aluno. Armazene todas as 
informações num dicionário. No final programa deve imprimir as informações do dicionário
e situação do aluno (reprovado, exame ou aprovado). Utilize as regras da
UNIFESP para definir a situação do aluno.
'''
aluno = {}

aluno['nome'] = str(input('Nome: ')).strip().title()
aluno['RA'] = int(input('RA: '))
aluno['Média'] = float(input('Média Final do Aluno: '))

print('-='*15)
for k,v in aluno.items():
    print(f'- {k}: {v}')
if aluno['Média'] >= 6:
    print('\033[32mAluno Aprovado!\033[m')
elif aluno['Média'] >= 3:
    print('\033[33mRecuperação\033[m')
else:
    print('\033[31mReprovado\033[m')
print('-='*15)
