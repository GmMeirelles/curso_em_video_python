tupla = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
par = 0
print(f'O número 9 foi digitado {tupla.count(9)} vezes')
print(f'O primeiro número 3 foi digitado na {tupla.index(3)+1} posição')
for n in tupla:
    if n % 2 == 0:
        par += 1
print(f'Dos números digitados {par} são pares')