'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso,
você deve mostrar, para cada palavra, quais são as suas vogais.
'''
palavras = ('CURSO','GRATUITO','PYTHON','ONLINE','PROGRAMADOR')
for p in palavras:
    print(f'Na palavra {p} temos as vogais: ',end='')
    for letra in p:
        if letra in 'AEIOUaeiou':
            print(f'{letra} ',end=' ')
    print('')