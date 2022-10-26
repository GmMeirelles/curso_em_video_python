from time import sleep

def linha():
    print('=-'*30)

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} pulando de {passo} em {passo}')
    if fim > inicio:
        for n in range(inicio, fim+1, passo):
            print(n, end=', ', flush=True)
            sleep(0.5)
        print('Fim')
    else:
        cont = inicio
        print(inicio, end=', ', flush=True)
        sleep(0.5)
        while cont != fim:
            cont -= passo
            print(cont, end=', ', flush=True)
            sleep(0.5)
        print('Fim')


# Programa Principal
linha()
contador(1, 10, 1)
linha()
contador(10, 0, 2)
linha()
i = int(input('Digite o inicio: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))
contador(i, f, p)