'''
2) Escreva um programa que leia 3 números e que imprima o maior e o menor
'''
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
num = [n1,n2,n3]

print(f'O menor valor digitado foi {min(num)}')
print(f'O maior valor digitado foi {max(num)}')
