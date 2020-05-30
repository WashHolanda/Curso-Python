'''
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10
primeiros termos da progressão usando a estrutura while.
'''
cont = 0
first = int(input('Digite o primeiro valor da PA: '))
razao = int(input('Digite a razão da PA: '))
print(first,end=' ')
while cont < 8:
    first += razao
    print(first,end=' ')
    cont += 1
print(first+razao)
