# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "São"

print('Digite o nome de uma cidade')
city = input('>>>  ').upper()


if city[0:3] == 'SÃO':
    print('A cidade começa com São, então podemos excluir uma grande parte das cidades')

else:
    print('A cidade não começa com São, oq exclui muitas possibilidades como: São Paulo, São Carlos, São João etc...')