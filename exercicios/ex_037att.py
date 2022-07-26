print('Escreva um numero inteiro')
num = int(input('>>>  '))
print('Okay agora digite a base de conversão do número')
um = input('1- binario\n2- octal\n3- hexadecimal\n>>>  ')
if um == '1':
    num_bin_list = ''
    resto = 0
    while num > 0:
        resto = num%2
        num = num//2
        num_bin_list += str(resto)

    print(''.join(list(reversed(num_bin_list))))

elif um == '2':
    num_oct_list = ''
    resto = 0
    while num > 0:
        resto = num%8
        num = num//8
        num_oct_list += str(resto)

    print(''.join(list(reversed(num_oct_list))))

else:
    print('OPÇÃO INVALIDA')
    