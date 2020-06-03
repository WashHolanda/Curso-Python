'''
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido 
quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no
final do jogo. 
'''
from random import randint
print('-='*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*15)
win = 0
poui = ' '
while 1:
    num = int(input('Digite um valor: '))
    while poui not in 'PI':
        poui = str(input('Par ou Ímpar [P/I]? ')).strip().upper()[0]
    pc =randint(0,11)
    print('-'*15)
    print(f'Você jogou {num} e o computador jogou {pc}',end = '.')
    soma = num + pc
    if (soma % 2) == 0:
        print(f'Total de {soma} DEU PAR!')
        if poui == 'P':
            print('\033[32mVOCÊ VENCEU!\033[m')
            print('Vamos jogar novamente...')
            win += 1
        else:
            print('\033[31mVOCÊ PERDEU!\033[m')
            break
    else:
        print(f'Total de {soma} DEU ÍMPAR!')
        if poui == 'I':
            print('\033[32mVOCÊ VENCEU!\033[m')
            print('Vamos jogar novamente...')
            win += 1
        else:
            print('\033[31mVOCÊ PERDEU!\033[m')
            break
print(f'\033[31mGAME OVER!\033[m Você venceu {win} vezes.')
