# leia um numero inteiro e diga se é primo

num1 = int(input('Digite um número: '))
total = 0
for c in range(1, num1 + 1, 1):
    if num1 % c == 0:
        total += +1
        d = print(f'{c} = Divisivel, ')
    else:
        print(f'{c}, ')

print(f'o número {num1} tem um total de {total} Divisiveis')
if total == 2:
    print(f'Oque faz o número {num1} ser Primo')

elif total > 2 or total < 2:
    print(f'Oque faz o número {num1} não ser Primo')
