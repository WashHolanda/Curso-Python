'''
2) Crie uma rotina que solicite uma frase ao usuário e retorne
o número de caracteres na frase e o número de espaços.
'''
frase = input('Digite uma frase qualquer: ')
print(f"""Número de caracteres da frase: {frase.__len__()}
O número de espaços na frase é: {frase.count(' ')}""")
