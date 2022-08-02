# teste para criar um jogo

from random import randint
from time import sleep

print('''Hoje iremos testar um teste da criação de um jogo
Vamos começar escolha uma das classes dentre essas
[1] Bárbaro
[2] Arqueiro
[3] Tank
[4] Assasino''')
classe = str(input('>>>  '))  # aqui o player escolhe sua classe
if classe == '1':
    print(f'''Okay vamos começar seu Bárbaro foi criado com status sortidos de Força, Vida e Velocidade.
    Sabendo disso seu Bárbaro ficou com estes status:''')
    print('=-='*40)
    força = randint(5, 10)
    vida = randint(50, 100)
    velocidade = randint(5, 10)
    print(f'Força:{força}\nVida:{vida}\nVelocidade:{velocidade}')
    print('=-='*40)
    
    print('''Perfeito agora decida aonde você quer começar a sua jornada:
    [1] Castelo do rei destruido
    [2] Cidade Fantasma
    [3] Floresta amaldiçoada''')
    local_começo = str(input('>>>  '))
    if local_começo == '1':
            print('=-='*40)
            print('Okay seu bárbaro parte bravamente para o cástelo do rei destruido\nOnde la ele encontra-ra criaturas e tésouros desconhecidos e ainda não explorados')
            print('Andando por dentro do castelo seu bárbaro encontra, gire o dado para descobrir oque é')
            print('=-='*40)
            input('Digite qualquer coisa para rodar o dado:')
            dado = randint(0, 3)
            print(f'Dado: {dado}')
            if dado <= 3:
                print('Droga você encontrou um zumbi com 20 de vida 5 de ataque e 5 de velocidade no castelo, oque você deseja fazer:\n[1] Atacar\n [2]Defender')
                ação = input('>>>  ')
                vi_z = int(20)
                at_z = int(5)
                ve_z = int(4)
                while vi_z > 0:
                    if ação == '1':
                        vi_z = vi_z - força
                        print(f'Você tira {força} de vida do zumbi, deixando ele com {vi_z} e ele revida com {at_z} deixando você com {vida-at_z}, oque deseja fazer agr\n >>>  ')
                    else:
                        print('você se defende, pulando a sua vez e fazendo com que o inimigo não te acertasse, oque deseja fazer agora?\n >>>  ')
                    

                    
# elif classe == '2':

# elif classe == '3':

# elif calsse == '4':

# else:
#     print('Escolha invalida!!!! Recomeçe o jogo e tente novamente')