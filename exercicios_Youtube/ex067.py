'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor 
digitado pelo usuário. O programa será interrompido quando o número solicitado for 
negativo. 
'''
while 1:
    num = int(input('Digite um valor para ver sua tabuada: '))
    if num < 0:
        break
    print('-'*13 )
    for i in range(1,10):
        print(f'{num}x{i}  =  {num*i}')
    print(f'{num}x10 =  {num*(i+1)}')
print('Programa de tabuada encerrado!')
