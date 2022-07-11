# um professor quer sortear um dos seus quatro alinos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

from random import choice

print('Irei sortear 4 alunos para ver quem vai apagar a lousa, quem quer tentar?')
n1 = input('Primeiro: ')
n2 = input('Segundo: ')
n3 = input('Terçeiro: ')
n4 = input('Quarto e ultimo: ')
print(f'Muito bem agora usando o sorteador de nomes oque vai cair vai ser: \n{choice([n1, n2, n3, n4])}')
