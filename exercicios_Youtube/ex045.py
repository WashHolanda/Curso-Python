'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''
from random import choice
from time import sleep
print('''Escolha entre: 
pedra
papel
tesoura''')
player = input('Qual a sua jogada? ').lower()
com = choice(['Pedra', 'Papel', 'Tesoura']).lower()
print('JO')
sleep(0.8)
print('KEN')
sleep(0.8)
print('PO!!!')
print('-='*10)
print(f'PLAYER jogou {player.title()}')
print(f'COM jogou {com.title()}')
print('-='*10)
if player == com:
    print('\033[33mEMPATE\033[m')
else:
    if (player == 'pedra' and com == 'tesoura') or (player == 'papel' and com == 'pedra') or (player == 'tesoura' and com == 'papel'):
        print('\033[32mVOCÊ VENCEU!\033[m')
    else:
        print('\033[31mVOCÊ PERDEU!\033[m')