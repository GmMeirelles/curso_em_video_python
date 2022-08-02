# leia o peso de 5 pessoas e diga qual pesa mais e qual pesa menos

maior = 0
menor = 0

for pessoa in range(1, 6):
    peso = float(input(f'Peso da {pessoa} Pessoa: '))
    if pessoa == 1:
        maior = pessoa
        menor = pessoa
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'Maior Peso: {maior}')
print(f'Menor peso: {menor}')
