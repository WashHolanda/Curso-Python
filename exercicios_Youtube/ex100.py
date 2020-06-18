'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e 
somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a 
segunda função vai mostrar a soma entre todos os valores pares sorteados pela função 
anterior.
'''
from random import randint
from time import sleep
def sorteia(num):
    print('Sorteando 5 valores da lista: ')
    sleep(1)
    for i in range(0,5):
        num.append(randint(0,100))
        print(f'{num[i]}',end=' ',flush=True)
        sleep(0.5)
    print('PRONTO!')
    somaPar(num)


def somaPar(num):
    soma = 0
    for i in num:
        if (i % 2) == 0:
            soma += i
    print(f'Somando os valores pares de {num}, temos {soma}')


números = []
sorteia(números)
