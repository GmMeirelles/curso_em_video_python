# se eu souber exatamente o que quero fazer no código e não precisar de tantas funções de uma biblioteca pode-se fazer:
from random import randint
from math import sqrt, ceil

num = randint(1, 10)
print(f"a raiz quadrada de {num} é igual a {ceil(sqrt(num))} (obs: o numero foi arredondado para cima)")

# não precisando usar o math.função 
# para encontrar outras funções entre no site do python
