'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano
de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto
NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''
def voto(ano):
    '''
    -> Função que indica se a pessoa precisa votar ou não.
    :param ano: Ano de nascimento.
    :return: Não possui.
    '''
    from datetime import date
    idade = date.today().year - ano
    if idade >= 18 and idade < 65:
        return f'Com {idade} anos: \033[32mVOTO OBRIGATÓRIO\033[m.'
    elif idade >= 16 or idade >= 65:
        return f'Com {idade} anos: \033[33mVOTO OPCIONAL\033[m.'
    else:
        return f'Com {idade} anos: \033[31mNÃO VOTA\033[m.'


print('-'*15)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
