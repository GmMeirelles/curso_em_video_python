# PA v3.0

print('Digite o termo inicial, e a constante de uma PA')
termo = int(input('>>>  '))
cons = int(input('>>>  '))
cont = 1
print(f'{termo}, ', end='')
while cont < 10:
    cont += 1
    termo = termo + cons
    print(f'{termo}, ', end='')
print('Fim')
