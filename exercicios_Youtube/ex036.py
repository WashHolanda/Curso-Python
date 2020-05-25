'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.
'''
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do Comprador: R$'))
anos = int(input('Quantos anos de Financiamento? '))
prestação = casa / (anos*12)
print(f'Para pagar um empréstimo de R${casa:.2f} em {anos} anos', end='')
print(f' e a prestação será de R${prestação:.2f}')
if prestação <= (salario*(30/100)):
    print('\033[1;32mEmpréstimo CONCEDIDO!\033[m')
else:
    print('\033[1;31mEmpréstimo NEGADO!\033[m')
    