# escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem: -O primeiro é maior -O segundo é maior - não existe valor maior, os dois sao iguais

print('Digite dois numeros e irei compara-los')
n1 = int(input('>>>  '))
n2 = int(input('>>>  '))

if n1 > n2:
    print('O primeiro valor é maior')

elif n1 < n2:
    print('O segundo valor é maior')

else:
    print('Não existe  valor maior, os dois são iguais')