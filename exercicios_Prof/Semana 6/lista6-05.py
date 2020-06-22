'''
5)Escreva  uma  função  chamada área_triang que  receba  a base e a altura de um triangulo e retorne sua área.
'''
def área_triang(base,alt):
    """ 
        -> Função que calcula a área de um triângulo.

    Args:
        base (float): Base do triângulo.
        alt (float): Altura do triângulo.
        
    Returns:
        float: Valor da área do triângulo.
    """
    area = (base*alt) / 2
    return area


base = float(input('Digite a base do triângulo: '))
altura = float(input('Digite a altura do triângulo: '))
print(f'A área do triângulo de base {base}cm e altura {altura}cm é {área_triang(base,altura)}cm²')
