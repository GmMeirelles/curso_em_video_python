# crie um programa que leia o nome completo de uma pessoa e mostre: 1- O nome com todas as letras maiúsculas 2- O nome com todas letras minúsculas 3- Quantas letras ao todo (Sem considerar espaços) 4- Quantas letras tem o primeiro nome

print('Digite seu nome completo')
nome = str(input('>>> ')).strip()
print('Analisando...')
print(f'Nome em maiúsculo: {nome.upper()}')
print(f'Nome em minúsculo: {nome.lower()}')
nse = int(nome.count(' '))
print(f'Tem ao todo de letras: {int(len(nome))-nse}')
nome.find(' ')
print('Primeiro nome: {}'.format((nome[0:nome.find(' ')])))
