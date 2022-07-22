# escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80kmh mostre uma mensagem dizendo que ele foi multado, a multa vai custar RS7,00 por cada Km acima do limite

from random import randint

v = randint(60, 100)
print(f'Bom dia meliante, eu tava vendo ali no meu radar de velocidade que você passou a {v}Km/h')
if v <= 80:
    print('E TA SUPER DENTRO DA FAIXA kkkkk só queria te assustar msm meu caro cidadão, pode continuar com a vida e tenha um Bom dia!!!')

else:
    print('ENTÃO MELIANTE VOCÊ ESTAVA PASSANDO ACIMA DO LIMITE DA VELOCIDADE DA ESTRADA')
    print('OQUE ISSO SIGNIFICA??? VOCÊ FOI MULTADO MELIANTEEEEE M U L T A D O ENTENDEU?')
    m = (v - 80)*7
    print(f'E COMO AQUI A MULTA É RS7.00 A CADA KM ULTRAPASSADO SUA MULTA SERA DE RS{m}.00')
    print('E CASO O SENHOR NÃO PAGAR ATE O PROXIMO MÊS TEU CARRO SERA CONFISCADO E REVISTADO, agradeço S2 e tenha um BOM DIA!!!!')