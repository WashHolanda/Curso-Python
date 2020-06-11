'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma
lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista 
ordenada na tela.
'''
lista = []
for i in range(0,5):
    num = int(input(f'Digite um valor: '))
    if i == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista!')
    else:
        if num in lista:
            lista.insert((lista.index(num)+1),num)
            print(f'Adicionado na posição {(lista.index(num)+1)} da lista!')
        else:
            for c,v in enumerate(lista):
                if v > num:
                    lista.insert(c, num)
                    print(f'Adicionado na posição {c} da lista!')
                    break
print(f'Os valores digitados, em ordem, foram: {lista}')
