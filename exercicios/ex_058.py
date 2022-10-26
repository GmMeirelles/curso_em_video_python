# melhore o desafio 28, contando quantas vezes o jogador vai errar

from random import randint
from time import sleep

tentativas = 1
pc = randint(1, 10)   # escolha do pc
print('<><>'*20)
print('Tente adivinhar o número que o PC pensará entre 1 e 5: ')
print('<><>'*20)
player = int(input('>>>  '))
sleep(1)

while player != pc:
    if player < pc:
        print('Mais... tente novamente')
        player = int(input('>>>  '))
        print('<><>'*20)
        tentativas += 1

    elif player > pc:
        print('Menos... tente novamente')
        player = int(input('>>>  '))
        print('<><>'*20)
        tentativas += 1

print(f'Acertou tentativas usadas: {tentativas}')
