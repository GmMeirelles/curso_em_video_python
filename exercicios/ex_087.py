matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = col3 = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input("Digite um número para a matriz: "))
print('-='*30)
for linha in range(0,3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]
    print()

print(f'Soma dos pares {pares}')
for linha in range(0, 3):
    col3 += matriz[linha][2]
print(f'Somam dos numeros da 3 coluna {col3}')
print(f'Maior valor da segunda coluna {max(matriz[1])}')