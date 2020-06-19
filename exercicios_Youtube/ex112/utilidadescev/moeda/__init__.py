def metade(valor,format=False):
    if format:
        return moeda(valor/2)
    else:
        return (valor/2)


def dobro(valor=0,format=False):
    if format:
        return moeda(valor*2)
    else:
        return (valor*2)
    

def aumentar(valor=0, porc=0,format=False):
    valor = valor * (1 +(porc/100))
    if format:
        return moeda(valor)
    else:
        return valor


def diminuir(valor=0, porc=0,format=False):
    valor = valor * (1 -(porc/100))
    if format:
        return moeda(valor)
    else:
        return valor


def moeda(valor=0, moeda='R$'):
    
    return f'{moeda}{valor:.2f}'.replace('.',',')


def resumo(valor=0, aumento=10, redução=5):
    print('-'*30)
    print('\033[30;47mRESUMO DO VALOR\033[m'.center(40))
    print('-'*30)
    print(f'Preço analisado:{moeda(valor):>14}')
    print(f'Dobro do preço:{moeda(dobro(valor)):>15}')
    print(f'Metade do preço:{moeda(metade(valor)):>14}')
    print(f'{aumento}% de aumento:{moeda(aumentar(valor,aumento)):>15}')
    print(f'{redução}% de redução:{moeda(diminuir(valor,redução)):>15}')
    print('-'*30)
