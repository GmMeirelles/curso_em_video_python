# o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import sample, shuffle

aluno1 = "Pedro"
aluno2 = "Matheus"
aluno3 = "Gabriel"
aluno4 = "Daniele"
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)

print("Olá alunos, hoje o grupo do Pedro ira apresentar o trabalho e para não ficar tão facil sortearei qual a ordem que cada um ira falar na apresentação")
print(f"E usando o aplicativo de sortear passado a ordem vai ser {sample([aluno1, aluno2, aluno3, aluno4], k=4)}")
print(f"TOMETOME CAVALO {lista}")