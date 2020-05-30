'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''
fat = 1
num = int(input('Digite um número: '))
print(f'Calculando {num}! = ',end='')
while num > 0:
    if num != 1:
        print(f'{num} x ',end='')
    fat *= num
    num -= 1
print(f'1 = {fat}')
'''
SOLUÇÃO ALTERNATIVA
from math import factorial
num = int(input('Digite um número: '))
print('O fatorial de {num} é {factorial(num)}')
'''
