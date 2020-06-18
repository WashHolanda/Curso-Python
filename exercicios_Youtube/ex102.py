'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro 
que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
'''
def fatorial(num,show=False):
    """
    -> Calcula o fatorial de um número
    :param num: O número que terá o fatorial calculado.
    :param show (opcional): Mostra ou não a conta passo a passo.
    :return: O valor do fatorial de um número.
    """
    fat = 1
    if show:
        for n in range(num,0,-1):
            if n == 1:
                print(f'{n} = ',end='')
            else:
                print(f'{n} x ',end='')
            fat *= n
    else:
        for n in range(1,num+1):
            fat *= n
    return fat

help(fatorial)
print(fatorial(5,show=True))
