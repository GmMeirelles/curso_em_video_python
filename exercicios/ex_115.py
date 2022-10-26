def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt())
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())


menu(['Criar arquivo',  'Cadastrar pessoas', 'Listar pessoas', 'Sair do sistema'])