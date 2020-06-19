'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(),
dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessasCrie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
funções.
'''
from moeda import metade,dobro,aumentar
preço = float(input('Digite o preço: R$'))
print(f'A metade de R${preço} é R${metade(preço):.2f}')
print(f'O dobro de R${preço} é R${dobro(preço):.2f}')
print(f'Aumentando 10% temos R${aumentar(preço,10):.2f}')
