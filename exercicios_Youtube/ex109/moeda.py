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
    return f'{moeda}{valor:.0f},00'