'''
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostra
uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima
do limite.
'''
velocidade = int(input('Qual a velocidade atual do carro? '))
if velocidade>80:
    print('\033[1;37;41mMultado! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade-80)*7
    print(f'Você deve pagar uma multa de R${multa:.2f}!\033[m')
print('Tenha um bom dia! Dirija com segurança!')
