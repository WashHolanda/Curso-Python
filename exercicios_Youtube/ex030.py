'''
Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar
'''
num = int(input('Digite um número: '))
if (num%2)==0:
    print(f'\033[0;33mO número {num} é PAR!')
else:
    print(f'\033[0;36mO número {num} é ÍMPAR!')
    