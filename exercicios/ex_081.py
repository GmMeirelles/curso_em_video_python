lista = []
cinco = cont = 0
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    cont += 1
    if num == 5:
        cinco += 1 
    continuar = input('Deseja continuar? [S/N] ')
    if continuar in 'Nn':
        break
lista.sort(reverse=True)
print(f'Quantidade de números digitados: {cont}\nNúmeros 5 encontrados na lista: {cinco}\nLista em ordem decrescente: {lista}')
