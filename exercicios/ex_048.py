# faça um programa que calcule a soma entre todos os números impares que são multiplos de treis no alcançe de 0 a 500

soma = 0

for c in range(1, 501, 2):
    if c%3 == 0:
        soma = soma + c
print(soma)