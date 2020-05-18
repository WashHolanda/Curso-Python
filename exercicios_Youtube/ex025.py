'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
'''
nome = input('Qual o seu nome completo? ').strip().lower()
print(f'Seu nome tem Silva? {"silva" in nome}')
