'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, 
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e 
mostrá-lo por extenso.
'''
num = int(input('Digite um número entre 0 e 20: '))
while num < 0 or num > 20:
    print('\033[31mTente novamente.\033[m', end=' ')
    num = int(input('Digite um número entre 0 e 20: '))
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
        'nove', 'dez', 'onze', 'doze', 'treze', 'quartorze', 'quinze', 'dezesseis', 
        'dezessete', 'dezoito', 'dezenove', 'vinte')
print(f'Você digitou o número \033[32m{extenso[num]}\033[m')
