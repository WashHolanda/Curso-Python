'''
1) Escreva uma função chamada fatorial para calcular o fatorial de um número inteiro.
'''
def fatorial(num):
    """
        -> Calcula o fatorial de um número
    
    Args:
        num (int): O número que terá o fatorial calculado.
    
    Returns:
        int: O valor do fatorial do número.
    """
    fat = 1
    for n in range(1,num+1):
        fat *= n
    return fat


num = int(input('Digite um valor: '))
print(f'O fatorial de {num} é {fatorial(num)}')
