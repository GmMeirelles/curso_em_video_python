# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo-retângulo, calcule e mostre o compromento da hipotenusa

from math import pow
c_o = int(input("Qual o comprimento do cateto oposto?: "))
c_ad = int(input("Qual o comprimento do cateto adjacente?: "))
c_h = c_o+c_ad
print(f"Bom segundo as medidas {c_o}² e {c_ad}² o cateto da hipotunusa é igual a {c_h}²")
print(f"O cumprimento total do cateto da hipotenusa é igual a {pow(c_h, 2):.0f}")