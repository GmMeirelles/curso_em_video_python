tot = 1
num = int(input('Digite um número: '))
soma = 0 
resp = input('deseja continuar? [S/N]: ').upper()
maior = 0
menor = 0
while resp == 'S':
    num += int(input('Digite um número: '))
    if tot == 1:
        maior = num
        menor = num
    
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = input('deseja continuar? [S/N]: ').upper()
    tot += 1
    soma += num
    
print(f'Total de números digitados: {tot}\nMédia dos números digiados: {soma//tot}\nMenor número: {menor}\nMaior número: {maior}')