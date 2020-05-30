'''
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos 
palpites foram necessários para vencer.
'''
from random import randint
from time import sleep
tent = 1
print('Vou pensar em um número entre 0 e 10. Tente Adivinhar...')
pc = randint(0,10)
print('Qual o seu palpite?')
player = int(input(''))
while player != pc:
    if pc > player:
        print(f'\033[1;31mMais...Tente mais uma vez.\033[m')
        player = int(input('Qual o seu novo palpite: '))
        tent += 1
    elif pc < player:
        print(f'\033[1;31mMenos...Tente mais uma vez.\033[m')
        player = int(input('Qual o seu novo palpite: '))
        tent += 1
else:
    print(f'\033[1;32mPARABÉNS! Você acertou com {tent} tentativa(s)!')
