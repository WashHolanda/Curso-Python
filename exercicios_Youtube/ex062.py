'''
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
'''
cont = 0
quant = 10
first = int(input('Digite o primeiro valor da PA: '))
razao = int(input('Digite a razão da PA: '))
print(first,end=' ')
while cont < 8:
    first += razao
    print(first,end=' ')
    cont += 1
first += razao
print(first)
adicional = int(input('Quantos termos você quer mostrar a mais? '))
while adicional != 0:
    cont2 = cont +adicional
    while cont < cont2:
        first += razao
        print(first,end=' ')
        cont += 1
    quant += adicional
    adicional = int(input('\nQuantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {quant} termos mostrados.')
