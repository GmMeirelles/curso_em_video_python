# faça um programa que leia uma frase e pelo teclado mostre: quantas vezes aparece a letra 'A' e em que posição ela aparece a primeira 

print('Escrava uma frase abaixo')
frase = str(input('>>>  '))
a = frase.count('a')
ac = frase.find('a')

print('Analises:')
print(f'Quantas vezes aparece a letra "A": {a}')
print(f'Aonde aparece pela primeira vez: {ac+1}')