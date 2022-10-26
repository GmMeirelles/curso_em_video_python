def fatorial(n, show=False):
    """
    fatorial(n, show=False)
        ->Calcula o fatorial de um numero:
        :param n: o número a ser calculado
        :param show: (opcional) Mostrar ou não a conta
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c} x ', end='')
        f *= c
    return f


print(fatorial(5, show=True))