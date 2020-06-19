'''
Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a 
mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
desenvolvida no desafio 108.
'''
from moeda import metade,dobro,aumentar,diminuir,moeda

preço = float(input('Digite o preço: R$'))
print(f'A metade de {moeda(preço)} é {metade(preço,format=True)}')
print(f'O dobro de {moeda(preço)} é {dobro(preço,format=True)}')
print(f'Aumentando 10% temos {aumentar(preço,10,format=True)}')
print(f'Reduzindo 10% temos {diminuir(preço,10,format=True)}')