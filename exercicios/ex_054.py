# grupo maior idade e menor idade

from datetime import date

total_menor = 0         # aqui criamos o total de pessoas de maior e menor
total_maior = 0

for pessoa in range(1, 8):          # aqui o for faz todo o codigo abaixo 7 vezes
    nasc = int(input(f'Qual a data de nascimento da {pessoa} Pessoa?  '))       # pergunta a data de nascimento
    idade = date.today().year - nasc                    # calcula a idade
    if idade >= 21:
        total_maior += +1           # adiciona +1 ao total de pessoas maior de idade

    else:
        total_menor += +1           # adiciona +1 ao total de pessoas menor de idade
print(f'Ao todo temos {total_maior} pessoas de maior\nE {total_menor} pessoas de menor')