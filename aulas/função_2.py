# help() usado para saber a utilidade de algum comando
help(print)

# para adicionar uma descrição ao seu codigo basta colocar """ no começo e """ na linha de baixo e no meio escrever a funcionalidade de sua função

def linha():
    """
    printa uma linha =-= com o tamanho de 60 caracteres
    """
    print('=-' * 30)


help(linha)
linha()

def somar(a, b, c=0): #isso serve para se caso o usuario n colocar o 3 parametro o parametro receber algum valor e não dar erro na função
    s = a + b + c
    print(s)

somar(1, 5, 4)
somar(1, 5)