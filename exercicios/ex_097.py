def escreva(msg):
    t = len(msg) + 5
    print('~' * (t))
    print(f'{msg:^{t}}')
    print('~' * (t))


# Programa Principal
escreva('URUGUTANGO_AZUL')
print()
print('Fim')