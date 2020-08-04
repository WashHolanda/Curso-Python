'''
3)Crie  uma  matriz  4  x  3  de  números  aleatórios  inteiros  no intervalo -5 a 5 e armazene em uma variável “mat”.
a)Escreva  um  comando  que  retorna  o  valor  absoluto  dos elementos dessa matriz.
b)Escreva   um   comando   que   retorna   o   seno   dos   valores contidos na primeira linha dessa matriz.
c)Escreva  um  comando  que  retorne  o  valor  máximo  das colunas da matriz
d)Calcule a soma dos elementos em cada coluna da matriz
e)Calcule a soma dos elementos em cada linha da matriz
f)Calcule  o  produto  entre  os  elementos  de  cada  coluna  da matriz. Dica: procure no google como resolver isso
'''
import numpy as np

mat = np.random.randint(0,11,(4,3),dtype='int64') - 5
print(mat)
print(f'Valores Absolutos: \n{np.abs(mat)}')
print(f'O seno dos valores da primeira linha: {np.sin(mat[0])}')
print(f'O valor maximo das colunas: {mat.max(0)}')
print(f'A soma dos elementos das colunas: {mat.sum(0)}')
print(f'A soma dos elementos das linhas: {mat.sum(1)}')