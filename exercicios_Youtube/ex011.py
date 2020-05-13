'''
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a
sua área e a quantidade de tinta necessária para pintá-la.
Sabendo que cada litro de tinta pinta uma área de 2m².
'''
larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
print(f'Sua parede tem a dimensão de {larg:.2f}x{alt:.2f} e sua área é de {larg*alt:.3f}m².')
tinta = larg*alt/2
print(f'Para pintar essa parede você precisará de {tinta:.2f}L de tinta.')
