'''
4) Escreva uma função chamada área_quad que recebe os lados de um retângulo e retorne sua área.
'''
def área_quad(larg,alt):
    """ 
        -> Função que calcula a área de um retângulo.

    Args:
        larg (float): Largura do retângulo.
        alt (float): Altura do retângulo.
        
    Returns:
        float: Valor da área do retângulo.
    """
    area = larg*alt
    return area


lado = float(input('Digite o lado do retângulo: '))
altura = float(input('Digite a altura do retângulo: '))
print(f'A área do retângulo de lado {lado}cm e altura {altura}cm é {área_quad(lado,altura)}cm²')
