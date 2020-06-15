'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No 
final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''
lista = []
pessoa = []
maior = menor = 0
op = ' '
while op != 'N':
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    lista.append(pessoa[:])
    pessoa.clear()
    op = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
print('-='*20)
print(f'Ao todo, você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {maior:.1f}Kg. Peso de: ',end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}',end=' ')
print('')
print(f'O menor peso foi de {menor:.1f}Kg.Peso de: ',end='')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}',end=' ')
print('')
