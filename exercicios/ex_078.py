valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {c}: ')))
print(f'O maior número digitado foi: {max(valores)} na posição {valores.index(max(valores))}')
print(f'O menor número digitado foi: {min(valores)} na posição {valores.index(min(valores))}')