'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma 
tabular.
'''
produtos = ('Lápis', 1.75, 'Caderno', 25.90, 'Transferidor', 4.20, 'Livro', 199.99)
print('-'*40)
#O caracter '^' centraliza o texto e o valor indicado mostra em que espaço o texto será colocado
print(f'{"LISTA DE PREÇOS":^40}')
print('-'*40)
for i in range(0,len(produtos)):
    if (i % 2) == 0:
#Os caracteres '>' e '<' se referem ao alinhamento do texto a esquerda ou direita e o '.' indica com oq será preenchido o espaço restante
        print(f'{produtos[i]:.<32}',end='')
    else:
        print(f'R${produtos[i]:>6.2f}')
print('-'*40)
