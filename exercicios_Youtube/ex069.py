'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o
programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. 
'''
mulheres = homens = maiores = 0
op = sexo = ' '
while 1:
    print(f'----- Cadastre uma Pessoa -----')
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = input('Sexo (M/F): ').strip().upper()
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
            mulheres += 1
    if idade > 18:
        maiores += 1
    while op not in 'SN':
        op = str(input('Quer continuar [S/N]? ')).strip().upper()
    if op == 'N':
        break
print(f'O total de pessoas com mais de 18 anos é {maiores}.')
if homens == 1:
    print(f'Ao todo temos {homens} homem cadastrado.')
else:
    print(f'Ao todo temos {homens} homens cadastrados.')
if mulheres == 1:
    print(f'E temos {mulheres} mulher com menos de 20 anos.')
else:
    print(f'E temos {mulheres} mulheres com menos de 20 anos.')
