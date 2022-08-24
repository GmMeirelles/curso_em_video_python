cinquenta = vinte = dez = um = 0
print('='*40)
print('{:^40}'.format('Banco MMc'))
print('='*40)
dinheiro = int(input('Digite a quantidade de dinheiro que deseja retirar: R$'))
while True:
    if dinheiro >= 50:
        dinheiro -= 50
        cinquenta += 1
    if dinheiro < 50:
        break
while True:
    if dinheiro >= 20:
        dinheiro -= 20
        vinte += 1
    if dinheiro < 20:
        break
while True:
    if dinheiro >= 10:
        dinheiro -= 10
        dez += 1
    if dinheiro < 10:
        break
while dinheiro != 0:
    dinheiro -= 1
    um += 1
print('=+'*20)
print('Você sacou:')
print(f'Cedulas de R$50: {cinquenta}\nCedulas de R$20: {vinte}\nCedulas de R$10: {dez}\nCedulas de R$1: {um}')
print('=+'*20)