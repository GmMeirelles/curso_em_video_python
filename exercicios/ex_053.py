# leia uma frase e diga se é palindromo

from time import sleep


frase = input('Escreva uma frase: ').upper().split()
frase = ''.join(frase)
frase_in = frase[::-1]
sleep(1)
print(f'Frase normal: {frase}\n')
sleep(0.5)
print(f'Frase invertida: {frase_in}\n')
sleep(1.5)

if frase == frase_in:
    print('=-='*20)
    print('Como podemos ver acima, a frase é um palíndromo')
    print('=-='*20)

else:
    print('=-='*20)
    print('Como podemos ver acima a frase não é um palindromo')
    print('=-='*20)







# print("Frase normal: ", ''.join(frase))
# print(f'Frase reversa: {"".join(frase[::-1])}')

# if frase == frase[::-1]:
#     print("Palindromo")