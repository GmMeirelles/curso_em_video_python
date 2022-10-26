pessoas = list()
dados = list()
cad = maior = menor = 0
while True:
    dados.append(input('Digite um nome: '))
    dados.append(float(input('Digite um peso: ')))
    if cad == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    cad += 1
    continuar = input("Deseja continuar? [S/N] ")
    if continuar in 'Nn':
        break
print(f'Pessoas cadastradas {cad} das pessoas')
print(f'Maior peso {menor} e maior peso {maior} das pessoas', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(p[0], end=' ')
    if p[1] == menor:
        print(p[0], end=' ')