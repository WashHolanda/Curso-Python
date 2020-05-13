'''
4) Faça um script que calcule o aumento de salário. Ele deve
solicitar o valor do salário e a porcentagem de aumento.
Exiba o valor do aumento e do novo salário.
'''
salario = float(input('Digite o valor do Salário: '))
porc = float(input('Digite a porcentagem do aumento: '))
aumento = salario*(1+(porc/100))
print(f'O Novo salário com {porc}% de aumento é R${aumento:.2f}')