'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
'''
from random import choice
nome1 = input('Primeiro Aluno: ')
nome2 = input('Segundo Aluno: ')
nome3 = input('Terceiro Aluno: ')
nome4 = input('Quarto Aluno: ')
lista = [nome1, nome2, nome3, nome4]
print(f'O aluno escolhido foi {choice(lista)}')
