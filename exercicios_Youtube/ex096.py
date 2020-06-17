'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um 
terreno retangular (largura e comprimento) e mostre a área do terreno.
'''
def área(l,c):
    print(f'A área de um terreno de {l:.1f}x{c:.1f} é de {(l*c)}m².')
    

print('Controle de Terrenos')
print('-'*20)
largura = float(input('Largura do terreno(m): '))
comprimento = float(input('Comprimento do terreno(m): '))
área(largura,comprimento)
