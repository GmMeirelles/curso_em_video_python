tot = -1
soma = -999
num = 0
while num != 999:
    num = int(input('Digite um número [O progama parara quando digitar 999]: '))
    soma += num
    tot += 1
print(f'Quantidade de números digitados {tot}\nSoma de todos os números digitados {soma}')
