n = 0
cont = 0
while True:
    n2 = int(input('Digite um número de 1 a 998 (use 999 para parar): '))
    if n2 == 999:
        break
    n += n2
    cont += 1
print(f'Você digitou {cont} números e a soma deles foi {n}')