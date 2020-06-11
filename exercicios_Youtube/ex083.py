'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu 
aplicativo deverá analisar se a expressão passada está com os parênteses abertos e 
fechados na ordem correta.
'''
exp = str(input('Digite a expressão: '))
certo = 0
for c in exp:
    if c == '(':
        certo += 1
    elif c == ')':
        certo -= 1
    elif certo < 0:
        break
if certo == 0:
    print('\033[32mSua expressão é válida!!\033[m')
else:
    print('\033[31mSua expressão não é válida\033[m')
