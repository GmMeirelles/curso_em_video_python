# faça um programa que calcule as duas notas de um aluno e mostre sua media

mat = str(input("Digite a matéria que você quer saber sua média: "))
not1 = int(input("Digite sua nota no primeiro bimestre dessa matéria: "))
not2 = int(input("Digite sua nota no segundo bimestre nessa matéria: "))
not3 = int(input("Digite sua nota no terceiro bimestre nessa matéria: "))
not4 = int(input("Digite sua nota no quarto bimestre nessa matéria: "))
med = (not1+not2+not3+not4)/4
print(f"Sua média em {mat} é igual a {med} Parabéns!")
