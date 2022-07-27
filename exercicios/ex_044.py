# programa que calcule o valor a ser pago por um produto

from time import sleep

p = float(input('Digite o valor do preço: R$'))
print('''Digite a forma de pagamento:
(1) A vista dinheiro/cheque (10% Desconto)
(2) À vista cartão (5% Desconto)
(3) 2x no cartão (Preço normal)
(4) 3x ou + no cartão (20% Juros)''')
dec = input('>>>  ')
print('PROCESSANDO...')
sleep(2)
if dec == '1':
    print(f'Á vista com dinheiro/cheque, preço com desconto: R${p-(p*0.10)}')

elif dec == '2':
    print(f'À vista com cartão, preço com desconto: R${p-(p*0.05)}')

elif dec == '3':
    print(f'2x no cartão, preço do produto: {p}')

elif dec == '4':
    print(f'3x ou + no cartão, preço com juros: {p+(p*0.2)}')

else:
    print('OPÇÃO INVALIDA!!')
