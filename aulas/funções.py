# você pode criar funções para usar codigos repetitivos como por exemplo
def linha():
    print('-'*30)


# Programa principal
print('Sistema de alunos')
linha()
print('Cadastro de alunos')
linha()
print('Fim')

print()
print('SEPARADOR')
print()

def tit(txt):
    print('-'*30)
    print(txt)
    print('-'*30)


tit(' Folheto ')
tit(' Armazem')

print()
print('SEPARADOR')
print()

def soma(a, b):
    s = a + b
    print(s)


soma(4, 6)
soma(a=5, b=9)
soma(b=7, a=9)

def contador(* num):  # com o *num ele guarda quantos valores forem necessarios na soma 2
    for v in num:
        print(v, end=' ')
    print('FIM!')


contador(5, 3, 2, 6, 7)
contador(3, 2, 1)
