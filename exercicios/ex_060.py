# fatorial de um número

numero = int(input('Digite um número: '))
numero_inicial = numero  # só para colocar o valor inicial na frase final (ignore)
resultado = numero

while numero > 1:
    numero -= 1
    resultado = resultado*(numero)
print(f'O Fatorial de {numero_inicial} é igual a {resultado}')
