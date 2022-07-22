# crie um programa que leia um número inteiro emostre na tela se ele é PAR ou IMPAR

print('DIGITE UM NUMERO INTEIRO')
n = int(input('>>>  '))
r = n%2
if r == 1:
    print('O numero Digitado é impar')

else:
    print('O numero digitado é par')