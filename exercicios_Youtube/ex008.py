'''
Escreva um programa que leia um valor em metros e o exiba convertido em todos os 
seus múltiplos e submúltiplos.
'''
metro = float(input('Digite uma distância em metros: '))
print(f'Km: {metro/1000}km\nHm: {metro/100}hm\nDam: {metro/10}dam')
print(f'dm: {metro*10}dm\ncm: {metro*100}cm\nmm: {metro*1000}mm')
