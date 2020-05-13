'''
Escreva um programa que converta uma temperatura digitada em ºC para ºF.
'''
celsius = float(input('Informe a temperatura em ºC: '))
fa = ((9*celsius)/5)+32
print(f'A temperatura de {celsius}ºC corresponde a {fa:.2f}ºF')
