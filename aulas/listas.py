# lista é como uma tupla só q mutavel e para criar usa-se []
lista = ['Macarrão', 'Hamburguer', 'Suco']
print(lista)
lista[2] = 'Sorvete'
print(lista)
#para adicionar um novo elemento a lista usasse append
lista.append('Cookie')
print(lista)
# pode colocar um item novo em algum lugar em especifico tbm
lista.insert(2, 'Chocolate')
print(lista)

#para apagar os lanches usa-se del ou pop
del lista[1]
print(lista)

# se não colocar um indice que não existe no pop ele excluira o ultimo
lista.pop(2)
print(lista)

lista.remove('Macarrão')
print(lista)

# para ordenar uma lista usasse
valores = [1, 5, 2, 7, 3, 9]
valores.sort()
print(valores)
valores.sort(reverse=True)
print(valores)

# a partir do momento que você cria outra lista utilizando a primeira vc esta vinculando as duas ou seja se você modificar valores2 vai modificar a valores tbm
valores2 = valores
valores2[3] = 5
print(valores)
print(valores2)

#para criar a copia de uma lista em outra usa-se
valores2 = valores[:]
