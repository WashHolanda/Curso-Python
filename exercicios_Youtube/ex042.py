'''
Refaça o EXERCICIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de
triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''
reta1 = float(input('Primeiro Segmento: '))
reta2 = float(input('Segundo Segmento: '))
reta3 = float(input('Terceiro Segmento: '))
if (reta1+reta2) > reta3 and (reta1+reta3) > reta2 and (reta2+reta3) > reta1:
    print('Os segmentos acima PODEM FORMAR um triângulo', end='')
    if reta1 != reta2 and reta1 != reta3 and reta2 != reta3:
        print(' \033[32mESCALENO\033[m')
    elif reta1 == reta2 == reta3 :
        print(' \033[32mEQUILÁTERO\033[m')
    else:
        print(' \033[32mISÓSCELES\033[m')
else:
    print('\033[31mOs segmentos acima NÃO PODEM FORMAR um triângulo!\033[m')
