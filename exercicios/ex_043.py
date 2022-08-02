# desenvolva uma lógica que leia  peso e a altura de uma pessoa, calcule seu imc e mostre seus status: abaixo de 18.5: abaixo do peso / entre 18.5 e 25: peso ideal / 25 até 30: sobrepeso / 30 até 40: obesidade / acima de 40: obesidade mórbida

print('Digite sua idade e seu peso, que calcularemos seu IMC (indíce de massa corporal)')
p = float(input('PESO: '))
a = float(input('ALTURA: '))
imc = p/(a**2)

print(f'IMC: {imc:.2f}')
if imc < 18.5:
    print('Peso abaixo da média')

elif imc > 18.5 and imc <= 25:
    print('Peso ideal')

elif imc > 25 and imc <= 30:
    print('Acima do peso')

elif imc > 30 and imc <= 40:
    print('ACIMA DO PESO!!')

else:
    print('OBESIDADE MÓRBIDA!!!! CUIDADO, COMECE A SE CUDIAR OU PODE TER SERIOS PROBLEMAS EM UM FUTURO PROXIMO')