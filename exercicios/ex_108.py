def metade(num=0.0):
    return num / 2


def dobro(num=0.0):
    return num * 2


def aumentar(num=0.0, aum=0):
    aumento = ((num * aum) / 100) + num
    return aumento


def diminuir(num=0.0, aum=0):
    resultado = num - ((num * aum) / 100)
    return resultado


def moedas(num=0.0, moeda='R$'):
    return f'{moeda}{num}'.replace('.', ',')


# Programa Principal
p = float(input('Digite o preço: '))
print(f'a metade de {moedas(p)} é {moedas(metade(p))}')
print(f'o dobro de {moedas(p)} é {moedas(dobro(p))}')
print(f'aumentando o preço em 10% do produto temos {moedas(aumentar(p, 10))}')