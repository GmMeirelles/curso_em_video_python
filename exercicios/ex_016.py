# crie um programa que leia um numero real qualquer pelo teclado e mostre sua porção inteira

from math import floor
from random import randrange, uniform

num1 = uniform(1, 10)
print(f"Numero real: {num1:.3f}")
print(f"porção inteira: {floor(num1)}")