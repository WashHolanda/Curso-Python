'''
5) Escreva um programa que pergunte o deposito inicial e a taxa de Juros de uma poupança.
Exiba os valores mês a mês para os 24 primeiros meses. No final deve imprimir o total de
ganho com juros no período.
'''
valor = float(input('Depósito Inicial: '))
taxa = float(input('Taxa de Juros da Poupança: '))
ganhos_totais = 0
for i in range(1,25):
    ganhos_totais += (valor*(taxa/100))
    valor = valor * (1 + (taxa/100))
    print(f'Mês {i}: R${valor:.2f}')
print(f'Ganhos Totais no período: R${ganhos_totais:.2f}')