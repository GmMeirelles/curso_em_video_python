# tupla = variavel que guarda mais de uma coisa
# para acessar algo dentro da tupla é representado por indices(numeros)
# ex: print(lanche[2])
# podendo tratar a variavel/string como na aula de tratamento de string
# LEMBRAR: "As tuplas são imutaveis"
# você não consegue mudar uma tupla dps de executar o programa o programa
# toda tupla é entre ()

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[-1])
print(lanche[-4])
print(lanche[:2])
print(lanche[-4:])
# lanche[4] = 'Chocolate quente' / aqui daria erro pois como dito acima tuplas sao imutaveis, ent n podemos mudar ela dps de ja escrita

for comida in lanche:
    print(f'eu comi {comida}')

print('-' * 40)

for cont in range(0, len(lanche)):
    print(f'eu comi {lanche[cont]}')

print('-' * 40)

a = (1, 5, 8, 4, 2)
b = (9, 7, 3, 2)
c = a + b  # utilizar sinal de mais para "somar" tuplas fazem elas se juntarem
print(c)
print(len(c))
print(c.count(2))
