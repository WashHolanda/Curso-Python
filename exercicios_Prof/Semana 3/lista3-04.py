'''
4) Desenvolva um programa que solicite o primeiro número de uma PA e sua razão.
O programa deve imprimir os 10 primeiros termos.
'''
first = int(input('Digite o primeiro valor da PA: '))
razao = float(input('Digite a razão da PA: '))
print(first,end=' ')
for i in range(0,8):
    first += razao
    print(first,end=' ')
print(first+razao)
