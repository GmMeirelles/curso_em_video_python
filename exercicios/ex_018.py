#faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente

from math import sin, cos, tan, radians

ang = int(input('Digite o ângulo que mostrarei o Seno, Cosseno e Tangente desse ângulo: '))
print(f'Seno: {sin(radians(ang)):.2f}')
print(f'Cosseno: {cos(radians(ang)):.2f}')
print(f'Tangente: {tan(radians(ang)):.2f}')