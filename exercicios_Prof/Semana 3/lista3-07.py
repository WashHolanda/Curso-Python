'''
7) Escreva um script que exibe a seguinte tábua de
multiplicação na tela:
1
2 4
3 6 9
4 8 12 16
5 10 15 20 25
'''
for i in range(1,6):
    print(i,end=' ')
    for j in range(2,i+1):
        print(i*j,end=' ')
    print('')
