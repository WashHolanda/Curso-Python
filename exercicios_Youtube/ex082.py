'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas
listas extras que vão conter apenas os valores pares e os valores ímpares digitados, 
respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''
lista = []
listaPar = []
listaImpar = []
op = ' '
while op not in 'N':
    num = int(input('Digite um valor: '))
    lista.append(num)
    if (num % 2) == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)
    op = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
print(f'A lista completa é {lista}')
print(f'A lista de pares é {listaPar}')
print(f'A lista de ímpares é {listaImpar}')
