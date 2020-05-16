'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
'''
from math import hypot
CO = float(input('Comprimento do Cateto Oposto: '))
CA = float(input('Comprimento do Cateto Adjacente: '))
print(f'A Hipotenusa vai medir {hypot(CO,CA):.2f}')
