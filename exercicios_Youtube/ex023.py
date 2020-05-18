'''
Faça um programa que leia um número de 0 a 9999 e motre na tela cada um dos seus
dígitos separados.
'''
# Método numérico de resolver
num = int(input('Informe um número: '))
print(f'Analisando o número {num}:')
print(f'Unidade: {(num%10)}')
print(f'Dezena: {((num%100)//10)}')
print(f'Centena: {(num%1000)//100}')
print(f'Milhar: {num//1000}')
