'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
sexo = input('Informe seu sexo [M/F]: ').strip().upper()[0]
while sexo not in 'MF':
    sexo = input('\033[31mDados Inválidos!\033[m Por favor informe seu sexo [M/F]: ').strip().upper()[0]
print(f'\033[32mSexo {sexo} registrado com sucesso!\033[m')
