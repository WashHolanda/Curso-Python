'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
op = 0
while op != 5:
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    op = int(input('Qual é a sua opção: '))
    if op == 1:
        print(f'A soma entre {num1} + {num2} é {num1+num2}')
        print('=-='*10)
    elif op == 2:
        print(f'A multiplicação entre {num1} x {num2} é {num1*num2}')
        print('=-='*10)
    elif op == 3:
        print(f'Entre {num1} e {num2} o maior valor é {max({num1,num2})}')
        print('=-='*10)
    elif op == 4:
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
        print('=-='*10)
