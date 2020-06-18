'''
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a 
função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt(‘Digite um n: ‘)
'''
def leiaInt(texto):
    entrada = input(texto)
    while not entrada.isnumeric():
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        entrada = input(texto)
    return int(entrada)


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
