'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde 
esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, 
sabendo que o vencedor tirou o maior número no dado.
'''
from random import randint
from time import sleep
from operator import itemgetter
ranking = {}
jogo ={'Jogador 1': randint(1,6),
        'Jogador 2': randint(1,6),
        'Jogador 3': randint(1,6),
        'Jogador 4': randint(1,6)}

print('-='*15)
print('Valores Sorteados: ')
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(),key=itemgetter(1),reverse=True)
print(f'{"Ranking":-^30}')
for k,v in enumerate(ranking):
    print(f'{k+1}º colocado: {v[0]}')
