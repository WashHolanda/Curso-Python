'''
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com 
valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o 
maior.
'''
from time import sleep
def maior(*num):
    print('Analisando os valores passados...')
    sleep(1.5)
    for n in range(0,len(num)):
        print(f'{num[n]}',end=' ',flush=True)
        sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo.')
    sleep(2)
    print(f'O maior valor informado foi {max(num)}.')
    sleep(2)


maior(3,8,6,1,12,9)
print('-='*20)
maior(3,8,6)
print('-='*20)
maior(5,1)
print('-='*20)
