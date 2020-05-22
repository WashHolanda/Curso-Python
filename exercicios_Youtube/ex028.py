'''
Escreva um programa que faça o computador "pensar" em um número inteiro de 0 a 10 
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deve escrever na tela se o usuário venceu ou perdeu.
'''
from random import randint
from time import sleep
print('Vou pensar em um número entre 0 e 10. Tente Adivinhar...')
pc = randint(0,10)
print('Em que número eu pensei?')
player = int(input(''))
print('PROCESSANDO...')
sleep(3)
if player == pc:
    print('PARABÉNS! Você me venceu!')
else:
    print(f'GANHEI! Eu pensei no número {pc} e não no {player}!')
