'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
num = int(input('Digite um número: '))
cont = 0
for i in range(1,num+1):
    if (num%i) == 0:
        print(f'\033[33m{i} \033[m',end=' ')
        cont += 1
    else:
        print(f'\033[31m{i} \033[m',end=' ')
print(f'\nO número {num} foi divisível {cont} vezes')
if cont == 2:
    print('\033[1;32mE por isso ele É PRIMO!\033[m')
else:
    print('\033[1;31mE por isso ele NÃO É PRIMO!\033[m')
