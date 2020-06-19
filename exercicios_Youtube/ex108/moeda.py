def metade(valor):
    return (valor/2)


def dobro(valor=0):
    return (valor*2)


def aumentar(valor=0, porc=0):
    valor = valor * (1 +(porc/100))
    return valor


def diminuir(valor=0, porc=0):
    valor = valor * (1 -(porc/100))
    return valor


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.0f},00'