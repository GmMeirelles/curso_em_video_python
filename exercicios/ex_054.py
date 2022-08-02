# grupo maior idade e menor idade

from datetime import date

total_maior = 0
total_menor = 0

for pessoa in range(1, 8):
    nasc = int(input(f'Qual a data de nascimento da {pessoa} Pessoa?  '))
    idade = date.today().year - nasc
    if idade >= 21:
        total_maior += +1

    else:
        total_menor += +1
print(f'Ao todo temos {total_maior} pessoas de maior\nE {total_menor} pessoas de menor')