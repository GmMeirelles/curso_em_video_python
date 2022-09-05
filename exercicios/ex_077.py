tupla = ('Macro', 'Computador', 'Videogame', 'Ladrilho', 'Londres')
for item in tupla:
    print(f'\nNa palavra {item} temos ', end='')
    for letra in item:
        if letra.lower() in 'aeiou':
            print(letra, end =' ')