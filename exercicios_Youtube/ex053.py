'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.
'''
frase = input('Digite uma frase: ').upper().strip()
palavras = frase.split()
semEspaços = ''.join(palavras)
inverso = ''
for i in range(len(semEspaços) - 1, -1, -1):
    inverso += semEspaços[i]
print(f'O inverso de {frase} é {inverso}')
if inverso == semEspaços:
    print('\033[32mTemos um palíndromo!\033[m')
else:
    print('\033[31mA frase digitada não é um palíndromo!\033[m')
