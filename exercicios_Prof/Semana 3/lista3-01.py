'''
1) Escreva um programa que pergunte a velocidade do carro de um usuário.
Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse
caso, exiba o valor da multa, cobrando 5 reais por Km acima de 80Km/h.
'''
velocidade = int(input('Qual a velocidade atual do carro? '))
if velocidade>80:
    print('\033[1;37;41mMultado! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade-80)*5
    print(f'Você deve pagar uma multa de R${multa:.2f}!\033[m')
print('Tenha um bom dia! Dirija com segurança!')