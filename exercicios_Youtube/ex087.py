'''
Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''
matriz = [[],[],[]]
somaPar = 0
somaTerc = 0
for i in range(0,3):
    for j in range(0,3):
        matriz[i].insert(j,int(input(f'Digite um valor para [{i+1},{j+1}]: ')))
        if (matriz[i][j] % 2) == 0:
            somaPar += matriz[i][j]
        if j == 2:
            somaTerc += matriz[i][j]
        if i == 1:
            if j == 0:
                maiorSeg = matriz[i][j]
            if matriz[i][j] > maiorSeg:
                maiorSeg = matriz[i][j]
print('-='*15)
for i in range(0,3):
    for j in range(0,3):
        print(f'{matriz[i][j]:>4}',end=' ')
    print('')
print('-='*15)
print(f'A soma dos valores pares é {somaPar}')
print(f'A soma dos valores da terceira coluna é {somaTerc}')
print(f'O maior valor da segunda linha é {maiorSeg}')
