def linha(tam=40):
    return '\033[m-'*tam


def cabeçalho(texto):
    print(linha())
    print(texto.center(40))
    print(linha())


def listaOpções(lista):
    for k,v in enumerate(lista):
        print(f'\033[33m{k+1} - \033[m',end='')    
        print(f'\033[34m{v}\033[m')
    print(linha())


def lerOpção(texto):
    while True:
        try:
            n = int(input(f'\033[33m{texto}\033[32m'))
        except:
            print('\033[31mERRO: Por favor, digite um número inteiro válido.\033[m')
        else:
            if n not in (1,2,3):
                print('\033[31mERRO: Por favor, digite uma opção válida!\033[m')
            else:
                break
    return n
