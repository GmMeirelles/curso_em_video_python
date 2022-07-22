# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem cobrando RS0.50 por Km para viagens de até 200Km e RS0.45 para viagens mais longas

print('Digite a distancia da viagem em Km')
v = int(input('>>>  '))
if v <= 200:
    print(f'Distãncia: {v}Km\nPreço: R${v*0.50:.2f}')

else:
    print(f'Distância: {v}Km\nPreço: R${v*0.45:.2f}')