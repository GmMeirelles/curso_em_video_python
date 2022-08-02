# refaça o desafio 009 de fazer uma tabuada usando o for

print('Digite um número que lhe mostrarei sua tabuada')
n = int(input('>>>  '))
x = 0
for c in range(1, 11):
    x = x+1
    print(f'{n} x {x} = {n*x}')