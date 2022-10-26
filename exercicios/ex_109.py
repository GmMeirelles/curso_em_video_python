def moedas(num=0.0, moeda='R$'):
    return f'{moeda}{num}'.replace('.', ',')


def metade(num, formato=False):
    resultado = num / 2
    if formato:
        return moedas(resultado)
    else:
        return resultado


def dobro(num, formato=False):
    resultado = num * 2
    if formato:
        return moedas(resultado)
    else:
        return resultado


def aumentar(num, aum, formato=False):
    aumento = ((num * aum) / 100) + num
    if formato:
        return moedas(aumento)
    else:
        return aumento


def diminuir(num, aum, formato=False):
    resultado = num - ((num * aum) / 100)
    if formato:
        return moedas(resultado)
    else:
        return resultado


#Programa inicial

valor = float(input('Digite o preço: R$'))
print(f'A metade de {moedas(valor, "R$")} é {metade(valor, formato=True)}')
print(f'O dobro de {moedas(valor)} é {dobro(valor, formato=True)}')
print(f'Aumentando 10% de {moedas(valor)}, temos {aumentar(valor, 10, formato=True)}')
print(f'Reduzindo 13% de {moedas(valor)}, temos {diminuir(valor, 13, formato=True)}')
