'''
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário
com 15% de aumento.
'''
salario = float(input('Qual o salário do funcionário: R$'))
aumento = salario*(1+(15/100))
print(f'O Novo salário com 15% de aumento é R${aumento:.2f}')