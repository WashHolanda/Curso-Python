'''
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: 
início, fim e passo. 
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''
from time import sleep
def contador(inicio,fim,passo):
    print(f'Contagem de {inicio} a {fim} de {abs(passo)} em {abs(passo)}')
    sleep(2)
    if passo > 0:
        if fim < inicio:
            passo *= -1
            fim -= 1
        else:
            fim += 1
    else:
        fim -= 1
    for i in range(inicio,fim,passo):
        print(f'{i}',end=' ', flush=True)
        sleep(0.5)
    print('FIM!')


print('-='*25)
contador(1,10,1)
print('-='*25)
contador(10,0,-2)
print('-='*25)
print('Agora é a sua vez de personalizar sua contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
print('-='*25)
contador(i,f,p)
print('-='*25)
