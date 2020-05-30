'''
Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
elementos de uma Sequência de Fibonacci. 
'''
print('-'*20)
print('Sequência FIBONACCI')
print('-'*20)
n = int(input('Quantos termos você quer mostrar?\n'))
cont = 0
fib1 = 0
fib2 = 1
print(fib1,end=' ')
print(fib2,end=' ')
while cont < n-2:
    fib = fib1 + fib2
    print(fib,end=' ')
    fib1 = fib2
    fib2 = fib
    cont += 1
print('')
