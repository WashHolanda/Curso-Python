'''
5) Crie um programa que leia nome, sexo, peso e altura de várias pessoas. guarde os dados
de cada pessoa num dicionário individual e acrescente o IMC da pessoa. Organize todos os 
dicionários em uma lista. No final mostre:
a. Quantas pessoas foram cadastradas
b. Qual é o peso médio das pessoas
c. Qual é a altura média das pessoas
d. Qual é IMC médio das pessoas
'''
listaPessoas = []
pessoa = {}
op = ' '
pesoMedio = alturaMedia = IMCmedio = 0

while op != 'N':
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: ')).strip().title()
    pessoa['Sexo'] = str(input('Sexo: ')).strip().upper()[0]
    pessoa['Peso'] = float(input('Peso: '))
    pessoa['Altura'] = float(input('Altura: '))
    pessoa['IMC'] = ((pessoa['Peso'])/(pessoa['Altura']**2))
    pesoMedio += pessoa['Peso']
    alturaMedia += pessoa['Altura']
    IMCmedio += pessoa['IMC']
    listaPessoas.append(pessoa.copy())
    op = str(input('Quer Continuar [S/N]? ')).strip().upper()[0]
print('-='*15)
print(f'Foram cadastradas {len(listaPessoas)} pessoas.')
print(f'O peso médio das pessoas cadastradas é de {(pesoMedio/len(listaPessoas)):.2f}Kg.')
print(f'A altura média das pessoas cadastradas é de {(alturaMedia/len(listaPessoas)):.2f}m.')
print(f'O IMC médio das pessoas cadastradas é de {(IMCmedio/len(listaPessoas)):.1f}')
