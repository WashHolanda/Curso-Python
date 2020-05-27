'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, 
mostre os 10 primeiros termos dessa progressão.
'''
first = int(input('Digite o primeiro valor da PA: '))
razao = float(input('Digite a razão da PA: '))
print(first,end=' ')
for i in range(0,8):
    first += razao
    print(first,end=' ')
print(first+razao)
