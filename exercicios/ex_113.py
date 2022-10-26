def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        
        except:
            print('Erro digite um número válido')
            

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
            return n

        except:
            print('Erro digite um número válido')


#Programa Principal
n = leiaint('Digite um inteiro: ')
n2 = leiafloat('Digite um real: ')
print(f'Intero = {n}\nReal = {n2}')