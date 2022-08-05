# leia o peso de 5 pessoas e diga qual pesa mais e qual pesa menos

maior = 0       # aqui cria a variavel da coisa mais pesada até o momento 
menor = 0       # e aqui da menor até o momento

for pessoa in range(1, 6):                  
    peso = float(input(f'Peso da {pessoa} Pessoa: '))           # pergunta o peso de 6 pessoas e guarda na variavel peso
    if pessoa == 1:                     # se for a primeira pessoa da lista, logo o maior e o menor peso vai ser dela
        maior = pessoa                              
        menor = pessoa
    else:                       # se não
        if peso > maior:           # se o peso da pessoa for maior q o antigo maior ele vai tomar o lugar do maior fazendo isso até chegar no final do laço de repetição
            maior = peso
        if peso < menor:           # se o peso da pessoa for menor q o antigo menor ele vai tomar o lugar do menor fazendo isso até chegar no final do laço de repetição
            menor = peso

# fazendo com que no fim do laço o maior peso fosse o maior colocado e o menor peso o menor colocado ai é só printar os pesos

print(f'Maior Peso: {maior}')
print(f'Menor peso: {menor}')
