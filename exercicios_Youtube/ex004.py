'''
Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo
e todas as informações possíveis sobre ele.
'''
n = input('Digite algo: ')
print('Tipo primitivo: ', (type(n)))
print('Alfanumérico?', n.isalnum())
print('Númerico?', n.isnumeric())
print('Alfabético?', n.isalpha())
print('Decimal?', n.isdecimal())
print('Minúsculo?', n.islower())
print('Maiúsculo?', n.isupper())
print('Digito?', n.isdigit())
print('Identificador?', n.isidentifier()) #Exemplo: 3a (Não pode ser usado com identificador, portanto FALSE)
print('Printable?', n.isprintable()) #retornará True quando todos os caracteres são visíveis quando manda imprimi-los
print('Espaço?', n.isspace())
print('Capitalizado?', n.istitle()) #Exemplo: "Palavra" (letra maiuscula e minuscula)
print('Verificação concluída')
