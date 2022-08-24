import random

w = 0
while True:
    valor = int(input('Digite um valor: '))
    escolha = input('Par ou Impar? [P/I] ').upper()
    valor_pc = random.randint(1, 5)
    calculo = (valor_pc + valor)%2 
    if escolha == "P":
        if calculo == 0:
            print('Você ganhou')
            w += 1
        else:
            print('Você perdeu')
            break
    elif escolha == 'I':
        if calculo == 0:
            print('Você perdeu')
            break
        else:
            print('Você ganhou')
            w +=1
print(f'Você ganhou {w} veze(s)')