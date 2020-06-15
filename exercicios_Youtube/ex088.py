'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai 
perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
'''
from random import randint
from time import sleep

lista = []
jogo = []

print('-'*35)
print(f'{"Números MEGA-SENA":^35}')
print('-'*35)
quant = int(input('Quantos jogos serão sorteados? '))
print('-'*8,f'SORTEANDO {quant} JOGOS','-'*8)
for i in range(0,quant):
    for n in range(0,6):
        num = randint(1,60)
        while num in jogo:
            num = randint(1,60)
        jogo.append(num)
    jogo.sort()
    print(f'Jogo {i+1}: {jogo}')
    lista.append(jogo[:])
    jogo.clear()
    sleep(1)
print(f'{"BOA SORTE!":-^35}')
