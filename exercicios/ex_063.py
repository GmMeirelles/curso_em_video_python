# Sequencia fibonnaci

print('-+'*20)
print('Digite um número inteiro: ')
print('-+'*20)
n = int(input('>>>  '))
n2 = n+n
c = 0
r = n2+n
print(f'{n}+{n} = {n2}', end=' /')
while c < 6:
    c += 1
    print(f' {n2} + {n} = {r}', end=' /')
    n = n2
    n2 = r
    r = n2 + n
