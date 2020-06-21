'''
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade 
da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat()
com a mesma funcionalidade.
'''
def leiaInt(texto):
    while True:
        try:
            entrada = int(input(texto))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        else:
            return entrada
    return int(entrada)


def leiaFloat(texto):
    while True:
        try:
            entrada = float(input(texto))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        else:
            return entrada
    return int(entrada)


i = leiaInt('Digite um Inteiro: ')
f = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {f}')
