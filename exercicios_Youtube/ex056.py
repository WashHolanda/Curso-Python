'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
mostre:
a média de idade do grupo;
qual é o nome do homem mais velho;
quantas mulheres têm menos de 20 anos.
'''
velho_idade = 0
media = 0
mulheres = 0
for i in range(0,4):
    print(f'----- {i+1}ª Pessoa -----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').upper()
    media += idade
    if sexo == 'M':
        if idade > velho_idade:
            velho_nome = nome
            velho_idade = idade
    else:
        if idade < 20:
            mulheres += 1
print(f'A média de idade do grupo é de {media/4} anos.')
print(f'O homem mais velho tem {velho_idade} anos e se chama {velho_nome}.')
if mulheres == 1:
    print(f'Ao todo há apenas {mulheres} mulher com menos de 20 anos')
else:
    print(f'Ao todo são {mulheres} mulheres com menos de 20 anos')
