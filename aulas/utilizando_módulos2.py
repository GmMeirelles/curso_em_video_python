# podemos fazer assim se quisessemos fazer a raiz quadrada de um numero e arredondar para cima por exemplo
import math

num = int(input("digite um numero inteiro: "))
print(f"a raiz quadrada de {num} é igual a {math.ceil(math.sqrt(num))} (obs: o numero foi arredondado para cima)")
