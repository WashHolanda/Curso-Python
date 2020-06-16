'''
3) Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos 
pelo teclado. No final, mostre a matriz na tela com a formatação correta.
'''
matriz = [[],[],[]]

for i in range(0,3):
    for j in range(0,3):
        matriz[i].insert(j,int(input(f'Digite um valor para [{i+1},{j+1}]: ')))
print('-='*15)
for i in range(0,3):
    print(f'{"|":>7}',end='')
    for j in range(0,3):
        print(f'{matriz[i][j]:>4}',end=' ')
    print(' |')
print('-='*15)
