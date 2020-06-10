'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
de Futebol (2019), na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.
'''
camp = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico Paranaense',
        'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 
        'Bahia', 'Vasco da Gama', 'Atlético Mineiro', 'Fluminense', 'Botafogo',
        'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('Lista da classificação final do Brasileirão 2019:')
for pos,time in enumerate(camp):
        print(f'{pos+1}º {time}')
print('-='*63)
print(f'\033[32mOs 5 primeiros colocados foram: ')
for pos,time in enumerate(camp[:5]):
        print(f'{pos+1}º {time}')
print('\033[m-='*63)
print(f'\033[31mOs times rebaixados foram: ')
for pos,time in enumerate(camp[-4:]):
        print(f'{pos+1}º {time}')
print('\033[m-='*63)
print('Lista dos times em Ordem Alfabética:')
print(sorted(camp))
print('-='*63)
print(f'A Chapecoense terminou na {camp.index("Chapecoense")+1}ª posição')
