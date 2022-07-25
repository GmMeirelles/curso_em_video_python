# escreva um programa que leia um número inteiro qualquer e peã para o usuário escolher qual será a base de conversão -1 para binario -2 para octal -3 para hexadecimal

print('Escreva um numero inteiro')
num = int(input('>>>  '))
print('Okay agora digite a base de conversão do número')
um = input('1- binario\n2- octal\n3- hexadecimal\n>>>  ')
if um == '1':
    num_bin_list = ""
    resto = 0

    while num > 0:
        resto = num%2
        num = num//2
        num_bin_list += str(resto)

    print(''.join(list(reversed(num_bin_list))))