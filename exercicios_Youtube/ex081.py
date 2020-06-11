'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''
lista = []
op = ' '
cont = 0
while op not in 'N':
    cont += 1
    num = int(input('Digite um valor: '))
    lista.append(num)
    op = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
lista.sort(reverse=True)
print(f'Você digitou {cont} elementos.')
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print('\033[32mO valor 5 foi encontrado na lista!\033[m')
else:
    print('\033[31mO valor 5 não foi encontrado na lista!\033[m')
