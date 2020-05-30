'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
num = int(input('Digite um número: '))
cont = 1
maior = menor = media = num
op = str(input('Quer Continuar? [S/N]: ')).strip().upper()[0]
while op == 'S':
    num = int(input('Digite um número: '))
    cont += 1
    media += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    op = input('Quer Continuar? [S/N]: ').strip().upper()[0]
print(f'Você digitou {cont} números e a média foi {media/cont}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
