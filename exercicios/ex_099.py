from random import randint
from time import sleep

def maior(* num):
    cont = maior = 0
    print('Analisando os parametros')
    for n in num:
        print(f'{n}', end=' ', flush=True)
        sleep(0.5)    
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print(f'Foram informados {cont} valores e o maior deles foi {maior}')
        

# Programa inicial
maior(randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))