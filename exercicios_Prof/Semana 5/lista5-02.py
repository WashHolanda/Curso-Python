'''
2)Escreva   uma   expressão   que   possa selecionar apenas   os elementos  de índice par   em   um  vetor,   independente   do tamanho do vetor. Teste essa expressão em alguns vetores da sua escolha.
'''
import numpy as np
from random import randint

m = np.random.randint(0,10,randint(1,10),)
print(m)
for k,v in enumerate(m):
    if k % 2 == 0:
        print(v)
