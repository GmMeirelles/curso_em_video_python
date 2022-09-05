from random import randint

rand = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
srand = sorted(rand)
print('Eu sorteei os valores: ', end=' ')
for n in rand:
    print(f'{n} ', end='')
print(f'\nMenor número: {srand[0]}')
print(f'Maior número: {srand[4]}')