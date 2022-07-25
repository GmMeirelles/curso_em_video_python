# if = se 
# else = senão
# elif = senão se
# usa-se dps de um if, podendo ter 1 if e varios elif sem else ou com else, mas lembre se nunk tera elif sem if

print(' digite duas notas que irei fazer uma média e dizer se é boa ou não')
num1 = float(input('>>>  '))
num2 = float(input('>>>  '))
med = (num1+num2)/2
if med <= 5:
    print('Com esta média você pode ficar de recuperação')

elif med >5 and med <8:
    print('Uma média boa mas da para melhorar')


else:
    print('Uma média ótima, ja da para passar de ano :D')
