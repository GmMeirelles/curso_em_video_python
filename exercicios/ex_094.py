galera = list()
pessoa = dict()
soma = média = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Qual nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo? [M/F]:  ')).upper() [0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro use apenas M ou F')
    pessoa['idade'] = int(input('Qual idade? '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())                                                        # aqui vai criar o dicionario pessoa perguntando os dados e por fim colocando uma copia desse dicionario com .append em uma lista
    while True:
        resp = input('Deseja continuar? [S/N]').upper() [0]
        if resp in 'SN':
            break
        print('Erro use apenas S ou N')
    if resp == 'N':
        break
print('=-'*30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas')                           # aqui mostra quantas pessoas foram cadastradas apenas verificando o tamanho da lista
média = soma /  len(galera)                                                 
print(f'A média das idades é {média:5.2f}')                                     
print('As mulheres são ', end=' ')
for p in galera:
    if p['sexo'] in 'Ff':                                                                   # aqui esta verificando o sexo  da pessoa para ver se é femonino, se for deve printar
        print(f'{p["nome"]}', end=' ')