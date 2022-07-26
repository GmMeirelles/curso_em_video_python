# faça um programa que leia a data de nascimento e informe de acordo com sua idade se ele ainda vai se alistar, se ja é a hora de se alistar, se ja passou o tempo de se alistar. o programa devera mostrar o tempo que falta ou que passou do prazo

from time import sleep
from datetime import date
# EX: 19/09/2005
data_nascimento = str(input('Digite sua data de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - int(data_nascimento[6:10])
print('PROCESSANDO...')
sleep(1.5)
if idade > 18:
    print(f'Você tem {idade} anos, ja se passaram {idade-18} anos da hora de se alistar, vagabundo')

elif idade == 18:
    print('Já esta na hora de se alistar, vá até o local de alistamento mais proximo')

elif idade < 18:
    print(f'De acordo com nossos registros você ainda tem {18-idade} anos antes de se alistar')

else:
    print('Idade Invalida')

