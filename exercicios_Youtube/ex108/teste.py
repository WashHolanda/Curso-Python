'''
Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga 
mostrar os números como um valor monetário formatado.
'''
from moeda import metade,dobro,aumentar,moeda

preço = float(input('Digite o preço: R$'))
print(f'A metade de {moeda(preço)} é {moeda(metade(preço))}')
print(f'O dobro de {moeda(preço)} é {moeda(dobro(preço))}')
print(f'Aumentando 10% temos {moeda(aumentar(preço,10))}')
