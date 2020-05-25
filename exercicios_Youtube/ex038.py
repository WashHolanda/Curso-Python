'''
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela
uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Os dois valores são iguais
'''
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
if num1 > num2:
    print('O \033[34mprimeiro\033[m valor é MAIOR')
elif num2 > num1:
    print('O \033[35msegundo\033[m valor é MAIOR')
else:
    print('Os dois valores são \033[33mIGUAIS\033[m')
