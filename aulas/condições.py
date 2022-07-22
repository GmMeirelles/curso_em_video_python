# if = se 
# elif = senão

print(' digite duas notas que irei fazer uma média e dizer se é boa ou não')
num1 = float(input('>>>  '))
num2 = float(input('>>>  '))
med = (num1+num2)/2
if med <= 5:
    print('Com esta média você pode ficar de recuperação')

else:
    print('Uma boa média, ja da para passar de ano :D')
