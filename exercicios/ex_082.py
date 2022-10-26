lista = []
continuar = ''

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    continuar = input('Quer continuar? [S/N] ')
    if continuar in 'Nn':
        break
print(f'Lista digitada: {lista}')
lista_par = []
lista_impar = []
for pos in lista:
    if pos % 2 == 0:
        lista_par.append(pos)
    else:
        lista_impar.append(pos)
print(f'Lista apenas com os pares: {lista_par}')
print(f'Lista apenas com os impares: {lista_impar}')