tot = ma_mil = menor = cont = 0
while True:
    produto = input('Digite o nome do produto: ')
    preço = float(input('Digite o preço do produto: R$'))
    tot += preço
    cont += 1
    continuar = input('Quer continuar? [S/N] ')
    if preço > 1000:
        ma_mil += 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    if continuar in 'Nn':
        break
print(f'Produto de menor preço foi {barato} e custa: R${menor}\nTotal: R${tot}\nQuantos produtos custaram mais que mil: {ma_mil}')