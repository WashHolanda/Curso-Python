'''
1) Crie uma rotina que solicite ao usuário dois lados de um
triângulo e ângulo , em graus, entre eles e retorna o
comprimento do terceiro lado. Use a lei dos cossenos.
'''
from math import sqrt,cos,radians
lado1 = float(input('Digite o tamanho do lado 1: '))
lado2 = float(input('Digite o tamanho do lado 2: '))
angle = float(input('Digite o angulo entre eles: '))

angle = radians(angle) #a função cosseno precisa do valor do angulo em radianos
lado3 = (lado1**2) + (lado2**2) - (2*lado1*lado2*cos(angle))
lado3 = sqrt(lado3)

print(f'O comprimento do terceiro lado do triãngulo é de {lado3:.2f}')
