# leia o sexo de uma pessoa, mas só aceite "M" ou "F" caso contrario pessa para digitar dnv

sexo = input('Digite o seu sexo (M = Masculino / F = Feminino): ').upper()      # pergunta o sexo do individuo
m = "M"
f = "F"
while sexo != m and sexo != f:              # enquanto sexo for diferente de m E diferente de F print:
    print('Resposta incorreta para os padrões do site, tente novamente')
    sexo = input('Digite o seu sexo (M = Masculino / F = Feminino): ').upper()
print('Okay Bem vindo(a) ao site')
