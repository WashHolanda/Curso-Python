'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
podem ou não formar um triângulo.
'''
print('-='*15)
print('Analisador de Triângulos')
print('-='*15)
reta1 = float(input('Primeiro Segmento: '))
reta2 = float(input('Segundo Segmento: '))
reta3 = float(input('Terceiro Segmento: '))
if (reta1+reta2) > reta3 and (reta1+reta3) > reta2 and (reta2+reta3) > reta1:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
    