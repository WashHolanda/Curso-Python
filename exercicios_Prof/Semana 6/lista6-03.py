'''
3) Escreva uma função que receba dois números e retorne True se o primeiro número for múltiplo do segundo.
'''
def multiplo(num1,num2):
    """
        -> Função que diz se um valor é múltiplo de outro.

    Args:
        num1 (int): Valor que a função tentará descobrir se é um múltiplo do valor 2 ou não.
        num2 (int): Valor que a função usará para avaliar o primeiro valor.

    Returns:
        bool: Retorno True se o valor 1 for um múltiplo do valor 2, caso contrário o retorno será False.
    """
    if (num1 % num2) == 0:
        return True
    else:
        return False



num1 = int(input('Valor 1: '))
num2 = int(input('Valor 2: '))

if multiplo(num1,num2):
    print(f'\033[32m{num1} é múltiplo de {num2}\033[m')
else:
    print(f'\033[31m{num1} não é múltiplo de {num2}\033[m')
