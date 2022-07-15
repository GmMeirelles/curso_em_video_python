import pygame

print('(obs: DIGITE TUDO EM MAISCULO)')
print('Olá Usuario, qual o seu nome?')
nome = input('>>>  ')
print(f'Olá {nome} tudo bem? hoje eu Meirelles quero testar um projeto criado por mim mesmo')
print('Onde esse programa imita um jogo de perguntas e respostas')
print('O programa ira lhe perguntar alguma coisa e vc tem que responder com sim ou não')
print('Preparado?')

resposta = input('>>>  ')
if resposta == "SIM":
    print('Okay vamos começar')

else:
    print("que triste ent vamos finalizar por aqui")
    input(">>>  ")
    quit()    

print("quanto é 2+2")
r1 = int(input('>>>  '))
if r1 == 4:
    print('Parabéns!!!')
    pontos = 0+1

else:
    print('ERRADOOOO')
    pontos = +0

print('Proxima pergunta :D')
print('Eu sou bonito? >.<')
r2 = input('>>>  ')
if r2 == 'SIM':
    print('CERTISSIMO BEBÊ')
    pontos = pontos+1

else:
    print('ERRADOOOO')
    pontos = pontos+0

print('Proxima pergunta :D')
print('Eu sou melhor que todo mundo no bloco fruta?')
r3 = input('>>>  ')
if r3 == "SIM":
    print("CORRETO!!!! é logico q sou melhor que todos")
    pontos = pontos+1

else:
    print("Errado!!!! EU SOU MELHOR QUE A FER999 >:C")
    pontos = pontos+0
print(f'Parabéns seus pontos finais são {pontos}')
if pontos == 3:
    print('Parabéns você tirou nota maxima')
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('projetos/correct.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait

else:
    print('HAHA NOOB VOCÊ NÃO TIROU NOTA MAXIMA HAHAHAHAHA')
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('projetos/errado.mp3')
    pygame.mixer.music.play()
    pygame.event.wait