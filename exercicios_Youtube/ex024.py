'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não
com a palavra "SANTO".
'''
cid = input('Em que cidade você nasceu? ').split()
cid[0] = cid[0].lower()
print(cid[0]=='santo')
