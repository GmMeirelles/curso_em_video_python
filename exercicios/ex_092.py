cadastro = {}
cadastro['nome'] = input('Digite seu nome: ')
cadastro['idade'] = int(input('Ano de nascimento: '))
cadastro['carteira'] = int(input('Carteira de trabalho (0 para não tem): '))
cadastro['idade'] = 2022 - cadastro['idade']
if cadastro['carteira'] == 0:
    print('=-='*30)
    for k, v in cadastro.items():
        print(f'{k} tem valor de {v}')
else:
    cadastro['contrato'] = int(input('Ano da contratação: '))
    cadastro['salario'] = int(input('Sálario R$'))
    print('=-='*30)
    for k, v in cadastro.items():
        print(f'{k} tem valor de {v}')