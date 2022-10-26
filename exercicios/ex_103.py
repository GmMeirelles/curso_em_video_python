def ficha(j = '<desconhecido>', g=0):
    print(f'jogador {j} fez {g} gols')


#Programa principal
nome = str(input('Nome do jogador: '))
gols = str(input('Quantidade de gols: '))

if gols.isnumeric():
    gols = int(gols)

else:
    gols = 0

if nome.strip() == '':
    ficha(g=gols)

else:
    ficha(nome, gols)