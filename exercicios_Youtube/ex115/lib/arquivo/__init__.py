from lib.menu import cabeçalho


def arquivoExiste(nome):
    try:
        arq = open(nome, 'rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[31mHouve um erro na criação do Arquivo!\033[m')
    else:
        print(f'\033[32mArquivo {nome} criado com sucesso!\033[m')


def lerArquivo(nome):
    try:
        arq = open(nome, 'rt')
    except:
        print('\033[31mErro ao ler o arquivo\033[m')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(arq.read())


def escreverArquivo(nome):
    try:
        arq = open(nome, 'at')
    except:
        print('\033[31mErro ao escrever no arquivo\033[m')
    else:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        while True:
            try:
                idade = int(input('Idade: '))
            except (ValueError, TypeError):
                print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            else:
                break
        pessoa = f'{nome:<30}{str(idade):>5} anos\n'
        arq.write(pessoa)
        print(f'\033[32mNovo registro de {nome} adicionado.\033[m')
