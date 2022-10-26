valores = []

while True:
    num = int(input('Digite um número: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado, não adicionado a lista...')

    continuar = input('Deseja continuar? [S/N] ')
    if continuar in 'Nn':
        break
valores.sort()
print(f'Valores em ordem crescente {valores}')