'''
6) Faça um programa que calcule a soma os números impares e múltiplos de 3 que se 
encontram no intervalo de 1 até 500.
'''
soma = 0
cont = 0
for i in range(1,501):
    if (i%3) == 0:
        if (i%2) ==1:
            soma += i
            cont += 1
print(f'A soma de todos os {cont} valores solicitados é {soma}')
