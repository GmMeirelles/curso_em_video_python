# escreva um programa que leia um número inteiro qualquer e peã para o usuário escolher qual será a base de conversão -1 para binario -2 para octal -3 para hexadecimal

print('Escreva um numero inteiro')
num = int(input('>>>  '))
print('Okay agora digite a base de conversão do número')
um = input('1- binario\n2- octal\n3- hexadecimal\n>>>  ')
if um == '1':
    print(f'{num} convertido para binário fica: {bin(num)}')

elif um == '2':
    print(f'{num} convertido para octal fica: {oct(num)}')

elif um == '3':
    print(f'{num} convertido para Hexadecimal fica: {hex(num)}')
