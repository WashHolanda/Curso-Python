'''
Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
visualização de detalhes do aproveitamento de cada jogador.
'''
jogador = {}
gols = []
time = []
op = ' '

while op != 'N':
    jogador['nome'] = str(input('Nome do Jogador: ')).strip().title()
    quant = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    for i in range(0,quant):
        gols.append(int(input(f'Quantos gols na {i+1}ª partida? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    gols.clear()
    jogador.clear()
    op = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
print('-='*30)
print(f'{"cod":<5}{"nome":<15}{"gols":<15}{"total":>10}')
print('-'*45)
for i,j in enumerate(time):
    print(f'{i:>3}  {j["nome"]:<15}{str(j["gols"]):<15}{j["total"]:>10}')
print('-'*45)
while True:
    num = int(input('Mostrar dados de qual jogador(-1 encerra o programa)? '))
    while num >= len(time):
        print('\033[31mO time não possui esse jogador, digite o código de um jogador válido ou -1 para encerrar.\033[m')
        num = int(input('Mostrar dados de qual jogador(-1 encerra o programa)? '))
    if num < 0:
        break
    print(f'Levantamento do jogador {time[num]["nome"]}')
    for i in range(0,len(time[num]['gols'])):
        print(f'    => Na partida {i+1}, fez {time[num]["gols"][i]} gols.')
    print(f'Foi um total de {time[num]["total"]} gols em todos os jogos.')
