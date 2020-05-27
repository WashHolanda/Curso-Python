'''
Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que 
agora utilizando um laço for.
'''
num = int(input('Digite um valor para ver sua tabuada: '))
print('-'*13 )
for i in range(1,10):
    print(f'{num}x{i}  =  {num*i}')
print(f'{num}x10 =  {num*(i+1)}')
