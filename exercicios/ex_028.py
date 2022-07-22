# escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça ao usuario tentar descobrir qual foi o numero escolhido pelo computador

import random

n = random.randint(1, 5)

print('Olá usúario hoje testaremos sua sorte \nCriamos um programa onde o computador escolhera um número aleatório entre 1 e 5\nDigite o numero que tu acha que o computador escolhera')
r = int(input('>>>  '))

if r == n:
    print('Parabéns!!! Você esta com uma sorte média hoje')

else:
    print('Que tristeza, sua sorte não esta em dia não recomendo apostar na mega cena kkk')
