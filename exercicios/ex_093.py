print('-'*12, end = '')
print('JOGADORES DE FUT', end = '')
print('-'*12)

jogador = dict()

jogador['nome' ] = input('Nome do jogador: ')
jogador['partidas'] = int(input('Partidas jogadas: '))
jogador['gols'] = []
#DEFININDO OS GOLS
for c in range(0, jogador['partidas']):
    jogador['gols'].append(int(input(f' Gols na {c+1}ª partida: ')))
jogador['total'] = sum(jogador['gols'])

print(f'O jogador {jogador["nome"]} fez um total de {jogador["total"]} gols nas suas {jogador["partidas"]} partidas.')
for k, s in enumerate(jogador['gols']):
    print(f'Partida {k+1}: {s} gols;')
