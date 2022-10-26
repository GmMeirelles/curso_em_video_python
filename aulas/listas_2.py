teste = list()
teste.append('João')
teste.append(19)
galera = list()
galera.append(teste[:]) # não se esquecer de colocar [:] para criar uma copia da lista teste antes de modificar se não iria sair duas vezes Marcos 16
teste[0] = 'Marcos'
teste[1] = 16
galera.append(teste[:])
print(galera)
print(galera[0][1]) # aqui vai pegar [0] da lista galera e o [1] da lista que ele pegar dentro da lista galera 
print("=_="*40)
for p in galera:
    print(p)    # aqui vai printar cada pessoa da lista e suas idades
    print(p[0]) # aqui vai printar só os nomes
    print(p[1]) # aqui vai printar só as idades
print('=--='*40)
galera2 = list()
dado = list()

for c in range(0, 3):                           
    dado.append(input('Digite um nome: '))
    dado.append(int(input('Digite uma idade: ')))       # aqui ele cria uma lista de dados para a pessoa escrever depois colocando uma copia da lista dados em galera e por ultimo limpando dados para na proxima repetição poder colocar novos dados
    galera2.append(dado[:])     
    dado.clear()