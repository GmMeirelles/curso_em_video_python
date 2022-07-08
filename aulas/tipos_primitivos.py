# str = palavras com '', int = numero inteiro, float = numero com ponto, bool = true e false

# definir definir o tipo primitivo antes de continuar

n1 = int(input("digite um numero: "))
n2 = int(input('digite outro numero: '))
s = n1 + n2
print('a soma entre {} e {} é igual a {}' .format(n1, n2, s))
# se tirar o int da variavel vai virar uma string ent o python ao invez de somar vai juntar os numeros