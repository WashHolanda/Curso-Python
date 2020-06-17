'''
4) Escreva uma função chamada área_quad que recebe os
lados de um retângulo e retorne sua área.
'''
def área_quad(l,a):
    area = l*a
    return area


lado = int(input('Digite o lado do retângulo: '))
altura = int(input('Digite a altura do retângulo: '))
print(f'A área do retângulo de lado {lado}cm e altura {altura}cm é {área_quad(lado,altura)}cm²')
