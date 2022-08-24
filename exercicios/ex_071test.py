cinquenta = vinte = dez = um = 0
print('='*40)
print('{:^40}'.format('Banco MMc'))
print('='*40)
dinheiro = int(input('Digite a quantidade de dinheiro que deseja retirar: R$'))
total = dinheiro
cedula = 50
totalcedulas = 0
while True:
    if total >= cedula:
        total -= cedula
        totalcedulas += 1
    else:
        print(f'Total de {totalcedulas} cedulas de {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedulas = 0
        if total == 0:
            break