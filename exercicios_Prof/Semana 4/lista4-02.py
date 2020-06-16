'''
2) Crie um programa onde o usuário possa digitar 10 valores numéricos e cadastre-os em 
2 listas separadas. Sendo a primeira contendo números primos e segunda não primos.
'''
listaPrimos = []
listaNprimos = []

for i in range(0,10):
    num = int(input('Digite um valor: '))
    flag_not = 0
    for n in range(2,num):
        if (num % n) == 0 and num != 2:
            flag_not = 1
            listaNprimos.append(num)
            break
    if num == 1:
        listaNprimos.append(num)    
    elif flag_not == 0:
        listaPrimos.append(num)
print(listaPrimos)
print(listaNprimos)
