from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
ranking = {}
for c in range(0, 4):
    jogadores[f'jogador{c}'] = randint(1, 6)
    print(f'jogador{c} rolou {jogadores[f"jogador{c}"]}')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True) # aqui esta arrumando a lista com base no indice 1 do dicionario que é o valor e por ultimo invertendo a lista para o vencedor ficar em primeiro
print(f'=-'*30)
c = 0
for k, v in ranking:
    print(f'{k} ficou em {c+1} lugar')
    c += 1
