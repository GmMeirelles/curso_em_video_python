# especie de calculadora

n1 = int(input('Digite um valor: '))
n2 = int(input('Ótimo digite outro valor: '))
print('''Perfeito agora escolha entre
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
escolha = str(input('>>>  '))

while escolha in '1, 2, 3, 4, 5':                       # erro de repetição infinita, pois ele vai ficar executando toda vez que tiver 1 2 3 4 ou 5 na escolha
    if escolha == '1':
        print(f'''A soma de {n1} e {n2} é igual a
        >>> {n1+n2} ''')
        exit()                  # arrumei colocando exit nos ifs para parar o while/programa

    elif escolha == '2':
        print(f'''A multiplicação de {n1} e {n2} é igual a
        >>> {n1*n2} ''')
        exit()
    
    elif escolha == '3':
        if n1 > n2:
            print(f'{n1} é o maior número')
            exit()
        else:
            print(f'{n2} é o maior número')
            exit()

    elif escolha == '4':
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Ótimo digite outro valor: '))
        escolha = str(input('>>>  '))

    else:
        exit()


print('Escolha Invalida')
escolha = str(input('Escolha entre 1 e 5: '))
    
