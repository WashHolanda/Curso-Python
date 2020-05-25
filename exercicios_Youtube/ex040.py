'''

'''
nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
media = (nota1+nota2)/2
print(f'Tirando {nota1:.2f} e {nota2:.2f}, a média do aluno será {media:.2f}')
if media >= 7:
    print('\033[1;32mAPROVADO!\033[m')
elif media >= 5 and media < 7:
    print('\033[1;33mRECUPERAÇÃO!\033[m')
else:
    print('\033[1;31mREPROVADO!\033[m')
