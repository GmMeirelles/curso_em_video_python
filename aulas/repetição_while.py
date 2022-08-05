# se você sabe o limite de repetições que terá que fazer é mais pratico utilizar a FOR, se n utilize a WHILE

from random import randint

maça = randint(0, 10)
personagem = 0

print(f'Maçã esta na {maça} posição')
while personagem != maça:
    print("Você ainda n chegou na maça (você anda mais um passo)")
    personagem += 1
print('Você chegou na maça')

# -----------------------------------------------------------------

c = 1
while c < 11:
    print(c)
    c += 1
print('Fim')

# -----------------------------------------------------------------

r = "S"
while r == "S":
    n = int(input("Digite um número: "))
    r = input(' Quer continuar [S/N]').upper()
print('FIM')

# ----------------------------------------------------------------

