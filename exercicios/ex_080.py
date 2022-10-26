valor = []

for c in range(0, 5):
    num = int(input('Digite um número: '))
    if c == 0:
        valor.append(num)
    elif c > 0 and c < 5:
        if num < valor[0]:
            valor.insert(0, num)
        
print(valor)