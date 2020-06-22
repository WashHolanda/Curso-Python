'''
2) Escreva uma função chamada maxnum que retorne o maior número de um conjunto de números. Utilize empacotamento para fazer a função.
'''
def maxnum(*conjunto):
    """Função que encontra o maior valor em um conjunto de números

    Returns:
        int: Maior valor encontrado no conjunto.
    """
    maior = max(conjunto)
    return maior


maior = maxnum(5,9,51,48,35,848,51,615,65,6,18,9)
print(maior)
maior = maxnum(3,5,9)
print(maior)
