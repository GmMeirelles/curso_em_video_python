# fatiar
# para fatiar uma frase coloque a variavel em que ela esta e o numero que vc quer entre colchetes, e se quiser separar uma parte da frase coloque [inicio:fim] porem isso exclui a ultima letra ent é bom colocar sempre um numero a mais 
# (obs: a primeira letra é considerada 0 ent vai de 0 até ...)
# pode se colocar outro : entre colchetes que significa quantas letras vai pular
frase = 'Olá mundo, Tudo bem?'
frase2 = '   Olá mundo, Tudo bem?     '
#        z1234567890123456789
print(frase[9])
print(frase[9:15])
print(frase[1:30:2])
# pode ler se frase[começo:fim:pulando 2 em 2]
print(frase[:3])
print(frase[11:])
print('-----------------------------------------------')

# analisar
print(len(frase))
# mostra o tamanho da frase
print(frase.count('o'))
# mostra o tanto de O que tem na frase, mas da pra fazer tbm
print(frase.count('o', 0, 13))
# que vai faze algo como o fatiamento, vai contar quantos O tem entre a letra 0 e 13 lembrando que remove a ultima letra (13)
print(frase.find('tud'))
# vai encontrar onde tem o 'tud' e mostrar onde começa, se o comando voltar com a posição -1 significa que não existe oque você pediu pra ele procurar na frase
'curso' in frase
# pode ler-se 'existe curso em frase', e vai voltar true ou false

# transformação
print(frase.replace('tudo bem', 'bão'))
# troca as frases
print(frase.upper())
print(frase.lower())
# a de cima transforma tudo em maiuscula e a de baixo tudo em minuscula
print(frase.capitalize())
print(frase.title()) 
# a  de cimajoga todas as letras pra minusculo e só deixa a letra inicial em maiuscula e o de baixo deixa toda palavra com a inicial em maiuscula
print(frase2.strip())
print(frase2.rstrip())
# exlui os espaços inuteis na frase do começo e do fim, o de baixo exclui apenas os inuteis do lado direito podendo trocar pra lstrip excluindo só os da esquerda

# divisão
frase.split()
# separa a frase aonde tem espaço resetando a contagem a cada palavra ficando gerando uma lista com todas palavras da frase
#'Olá mundo, Tudo bem?'
# z12 z12345 z123 z123


