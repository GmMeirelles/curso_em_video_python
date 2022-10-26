# dicionario usa-se quando quer ter um indice literario em uma lista
dados = dict() #ou dados = {} para criar um dicionario
dados = {'nome':'Pedro', 'idade':'17'}
print(dados['nome'])
print(dados['idade'])
# para criar um elemento novo dentro do dicionario sem mecher la em cima usa-se
dados['sexo'] = 'M'
# obs: .append n funfa em dicionario
print(dados['sexo'])
# del dados['idade'] para excluir algo dentro do dicionario
# decorar oq é valor, item e chaves
# valor = 
print(dados.values()) # valores pega somente os valores dos indices personalizados
print(dados.keys()) # keys pega somente os indices personalizados
print(dados.items()) # items pega os dois acima
print('=-'*30)
for k, v in dados.items():
    print(f'o {k} é {v}')
print('=-'*30)
# da para colocar varios dicionarios em uma lista tambem
brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'Sp'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[1]['sigla'])
    