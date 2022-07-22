# para colorir o terminal tem diversos modos mas o padão internacional é o ANSI usando:
# \033[0:33:44m
# começando com \ código para cor [estilo:texto:fundom
# alguns dos estilos são 0 nada, 1 negrito, 4 sublinhado e 7 negative
# cores vão de 30 ao 37
# fundo vão de 40 a 47
# usando em código:

print('\033[0,35,43mOlá Mundo')

# assim a lista do fundo vai até o fim mas se colocar \033[m no fim a lista para

print('\033[0,37,45mOlá Mundo\033[m')