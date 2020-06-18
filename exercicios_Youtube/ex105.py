'''
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e 
vai retornar um dicionário com as seguintes informações:

– Quantidade de notas                        
– A maior nota                                                                          
– A menor nota                                                                        
– A média da turma                                                                     
– A situação (opcional)
'''
def notas(*notas, sit=False):
    infos = {}
    média = 0
    infos['total'] = len(notas)
    infos['maior'] = max(notas)
    infos['menor'] = min(notas)
    infos['média'] = (sum(notas)/len(notas))
    if sit:
        if infos['média'] > 7 :
            infos['situação'] = 'BOA'
        elif infos['média'] > 5:
             infos['situação'] = 'RAZOÁVEL'
        else:
            infos['situação'] = 'RUIM'
    return infos


resp = notas(5.5, 10, 9.5, 6.5,sit=True)
print(resp)
