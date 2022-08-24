
n = 0

while True:
    print('=+='*20)
    n = int(input('Digite um número (digite -1 para acabar o programa): '))
    if n < 0:
        break
    if n > -1:
        print('=+='*20)
        c = 0
        while c < 10:
            c += 1
            print(f'{n} X {c} = {n*c}')
