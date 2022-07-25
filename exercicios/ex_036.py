# Escreva um programa qpara aprovar o empréstimo bancário para uma compra de uma casa. O programa vai perguntar o valor da casa, o sálario do comprador e em quantos anos ele vai pagar. Carlcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo sera negado

from time import sleep
print('Digite Seu Salário mensal, o valor da casa que quer comprar e em quantos anos você quer pagar')
print('(obs: náo use virgulas ou letras apenas o numero ex: 1250)')
sal = int(input('Salário: '))
casa = int(input('Preço da casa: '))
anos = int(input('Anos de pagamento: '))
am = anos*12
p = am/casa

if p <= sal*0.3:
    print(f'Desculpe mas a parcela da casa seria em torno de R${p} por mes oque pode significar que o senhor(a) tenha problemas ao pagar')
    sleep(4)
    print('fazendo com que a empreza preferisse não deixar o senhor pagar tais parcelas')

elif sal*0.3 > p:
    print(f'Tudo bem, iremos agendar o pagamento de {am} parcelas por R${p} Obrigado pela cooperação e aguarde o email que enviaremos no prazo valido de 24hrs')
