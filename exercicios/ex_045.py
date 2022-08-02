# crie um programa que jogue jokenpo com você

from random import shuffle
from time import sleep

print('''Vamos brincar um pouco, vamos jogar Jokenpô
eu irei escolher aleatóriamente entre: Pedra, Papel e Tesoura e você tera que adivinhar qual irei escolher
sabendo que Pedra > Tesoura > Papel > Pedra
Vamos começar qual sua escolha?''')
player = str(input(">>>  ")).capitalize()              # aqui o player escolhe oque quer
pc_list = ['Pedra', 'Tesoura', 'Papel']
shuffle(pc_list)
pc = pc_list[1]
('no ja ein, sem escalar')
sleep(1)
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Pô')
sleep(1)

if player in pc_list:
    if (player == "Tesoura" and pc == "Pedra") or (player == "Papel" and pc == "Tesoura") or (player == "Pedra" and pc == "Papel"):
        print("PC: HAHA, dessa vez eu ganhei!!!")
    
    elif player == pc:
        print("PC: Empate")

    elif (player == "Pedra" and pc == "Tesoura") or (player == "Papel" and pc == "Pedra") or (player == "Tesoura" and pc == "Papel"):
        print("PC: Droga, perdi mas só dessa vez ein")

    print(f'Aliás eu escolhi {pc}')
else:
    print('OPÇÃO INVALIDA!!!')
