'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em 
uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão 
exibidos todos os valores únicos digitados, em ordem crescente. 
'''
lista = []
op = ' '
while op not in 'N':
    num = int(input('Digite um valor: '))
    if num in lista:
        print('\033[31mValor Duplicado! Não foi possível adicionar o valor digitado.\033[m')
    else:
        print('\033[32mValor adicionado com sucesso!\033[m')
        lista.append(num)
    op = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
lista.sort()
print(f'Você digitou os valores {lista}')
