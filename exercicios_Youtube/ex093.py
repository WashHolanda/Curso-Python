'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai 
ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols 
feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o 
total de gols feitos durante o campeonato.
'''
jogador = {}
gols = []

jogador['nome'] = str(input('Nome do Jogador: '))
quant = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
for i in range(0,quant):
    gols.append(int(input(f'Quantos gols na {i+1}ª partida? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-='*20)
print(jogador)
print('-='*20)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*20)
print(f'O jogador {jogador["nome"]} jogou {quant} partidas.')
for i in range(0,quant):
    print(f'    => Na partida {i+1}, fez {jogador["gols"][i]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
