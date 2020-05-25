'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão:
- 1 para Binário
- 2 para Octal
- 3 para Hexadecimal
'''
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
op = int(input('Sua opção: '))
if op == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)}')
elif op == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)}')
elif op == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)}')
else:
    print('Opção Inválida! Tente Novamente!')
