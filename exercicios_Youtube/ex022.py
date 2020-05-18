'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras tem o nome ao todo.(Sem considerar os Espaços)
- Quantas letras tem o primeiro nome.
'''
nome = input('Digite seu nome completo: ').strip()
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome ao todo tem {(len(nome)-nome.count(" "))} letras.')
nome = nome.split()
print(f'Seu primeiro nome é {nome[0]} e ele tem {len(nome[0])} letras.')
