'''
3) Escreva um script que leia a quantidade de dias,horas,
minutos e segundos para o usuário. Calcule o total em
segundos.
'''
dias = int(input('Dias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))

total = segundos+(minutos*60)+(horas*3600)+(dias*24*3600)
print(f'Total de Segundos = {total}')