# aquele de calcular a média q eu ja fiz só que estou fazendo dnv

print('Abaixo Digite a nota dos 4 bimestre que irei dizer seu caso entre REPROVADO, RECUPERAÇÃO E/OU APROVADO')
n1 = float(input('>>>  '))
n2 = float(input('>>>  '))
n3 = float(input('>>>  '))
n4 = float(input('>>>  '))
m = (n1+n2+n3+n4)/4

if m <=5:
    print(f'Média: {m}\n REPROVADO')

elif m > 5.1 and m < 7:
    print(f'Média: {m}\n RECUPERAÇÃO')

else:
    print(f'Média: {m}\n APROVADO')