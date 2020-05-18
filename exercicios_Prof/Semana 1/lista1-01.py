"""
1) Crie um script em Python que solicite o nome, altura e peso
de uma pessoa e mostre a seguinte mensagem: “João tem
90 kilos e altura de 1.78 e portanto o IMC é de 28.4”.
"""
nome = input('Digite o seu nome: ')
altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))

IMC = peso/(altura*altura)
print(f"{nome} tem {peso} kilos e altura de {altura:.2f} e portanto o IMC é de {IMC:.2f}")
