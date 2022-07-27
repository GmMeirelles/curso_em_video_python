# a confederação nacional de natação le o ano de nascimento de um atleta e mostra sua categoria de acordo com idade: -até 9 anos = MIRIM    -até 14 anos = INFANTIL     -até 19 anos = JUNIOR   -até 20 anos = SÉNIOR  -acima = MASTER

from datetime import date
nasc = int(input('Digite seu ano de nascimento: '))
id = date.today().year - nasc

if id <= 9:
    print(f'Com {id} anos você está na categoria: MIRIM')

elif id > 9 and id <= 14:
    print(f'Com {id} anos você está na categoria: INFANTIL')

elif id > 14 and id <=19:
    print(f'Com {id} anos você está na categoria: JUNIOR')

elif id == 20:
    print(f'Com {id} anos você está na categoria: SÉNIOR')

else:
    print(f'Com {id} anos você está na categoria: MASTER')