# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo-retângulo, calcule e mostre o compromento da hipotenusa

import math
c_o =float(input("Qual o comprimento do cateto oposto?: "))
c_ad = float(input("Qual o comprimento do cateto adjacente?: "))
c_h = math.hypot(c_o, c_ad)
print(f"Bom segundo as medidas {c_o} e {c_ad} o cateto da hipotunusa é igual a {c_h:.3f}")