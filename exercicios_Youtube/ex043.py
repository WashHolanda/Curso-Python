'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de
Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''
peso = float(input('Qual é seu peso?(Kg): '))
altura = float(input('Qual é sua altura?(m): '))
imc = peso/altura**2
print(f'O IMC  dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Você está \033[33mABAIXO DO PESO\033[m normal!')
elif imc < 25:
    print('\033[1;32mParabéns, você está na faixa de PESO NORMAL\033[m')
elif imc < 30:
    print('Você está com \033[33mSOBREPESO!\033[m')
elif imc < 40:
    print('Você está com \033[31mOBESIDADE\033[m')
else:
    print('Você está \033[1;31mOBESIDADE MÓRBIDA CUIDADO!\033[m')
