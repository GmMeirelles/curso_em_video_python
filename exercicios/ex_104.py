def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Erro Digite um número inteiro')
        if ok:
            break
    return valor


#Programa principal
n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')
