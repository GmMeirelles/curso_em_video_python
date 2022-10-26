nome = input('Nome do aluno: ')
media = float(input('Media do aluno: '))
if media < 6:
    status = 'Reprovado'
else:
    status = 'Aprovado'

aluno = {'nome':nome, 'media':media, 'status':status}
for k, v in aluno.items():
    print(f' - {k}: {v}')
