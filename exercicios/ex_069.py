maior_dezoito = homens = mulher_vinte = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo: ')
    continuar = input('Deseja continuar? [S/N]: ')
    if idade > 18:
        maior_dezoito += 1
    if sexo in "Hh":
        homens += 1
    if idade >= 20 and sexo in "Ff":
        mulher_vinte
    if continuar in 'Nn':
        break
print(f'Você cadastrou:\n{homens} Homens\n{maior_dezoito} Maiores de 18 anos mulheres e homens\n{mulher_vinte} Mulheres maiores de 20 anos')