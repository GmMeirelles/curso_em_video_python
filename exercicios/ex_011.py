# faça um programa que calcule a area de uma parede e calcule quantos litros de tinta são necessarios para pinta-la sabendo que cada balde pinta uma area de 2m quadrado

print("Digite a altura da parede e depois a largura")
alt = int(input(">>>  "))
larg = int(input(">>>  "))
area = alt*larg
print (f"Considerando as medidas dadas a area total da parede em metros é {area}m^2 \nE seriam necessarios {area/2:.0f}L de tinta para pintar a parede inteira")