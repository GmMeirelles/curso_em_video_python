# escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento, para salarios superiores a R$1.250.00, calcule um aumento de 10%, para iguais ou inferiores aumento de 15%

s = float(input('Qual seu salário?: '))
a1 = s*0.15+s
a2 = s*0.10+s
if s <= 1250:
    print(f'Parabéns, com seu aumento de 15 porcento, seu salário vai de\n R${s} para R${a1} com o aumento de R${s*0.15}')

else:
    print(f'Parabéns, seu salario teve um aumento de {s*0.10} fazendo com que seu salario de {s} fosse para {a2}')
