'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''
pessoa = {}
listaPessoas = []
op = ' '
média = 0

while op != 'N':
    pessoa['Nome'] = str(input('Nome: ')).strip().title()
    pessoa['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while pessoa['Sexo'] not in 'MF':
        print('\033[31mERRO! Por favor, digite apenas M ou F.\033[m')
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    pessoa['Idade'] = int(input('Idade: '))
    média += pessoa['Idade']
    listaPessoas.append(pessoa.copy())
    pessoa.clear()
    op = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    while op not in 'SN':
        print('\033[31mERRO! Por favor, digite apenas S ou N.\033[m')
        op = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
print('-='*20)
print(f'A) Ao todo temos {len(listaPessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {média/len(listaPessoas)} anos.')
print(f'C) As mulheres cadastradas foram a',end=' ')
for i in listaPessoas:
    if i['Sexo'] == 'F':
        print(f'{i["Nome"]} e',end=' ')
print()
print(f'D) Lista de pessoas que estão acima da média de idade: ')
for i in listaPessoas:
    if i['Idade'] > (média/len(listaPessoas)):
        print('     ',end='')
        for k,v in i.items():
            print(f'{k} = {v};',end='')
        print('')
