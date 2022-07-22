# crie um programa que lê um ano qualquer e fala se é bissexto ou não

from random import randint
ano = randint(1, 4000)
print(f'Ano: {ano}')
bi = ano % 4
if bi != 0:
    print('Não é um ano Bissexto')

else:
    print('É um ano Bissexto')
