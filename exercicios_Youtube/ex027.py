'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
o primeiro e o último nome separadamente.
'''
nome = input('Digite o seu nome completo: ')
nome = nome.split()
print(f'Primeiro Nome: {nome[0]}')
print(f'Último Nome: {nome[(len(nome)-1)]}')
