def notas(*num, sit=False):
    """
    -> Função para analisar notas e situações de alunos.
    :param n: nota do aluno (Aceita varias).
    :praam sit: (Opcional) mostra a situação do aluno com base nas notas
    :return: dicionario com algumas informações com base na(s) nota(s) do aluno
    """
    
    list = dict()
    list['total'] = len(num)
    list['maior'] = max(num)
    list['menor'] = min(num)
    list['media'] = sum(num) / len(num)
    if sit:
        if list['media'] < 5:
            list['situação'] = 'REPROVA TUTO'
        else:
            list['sitação'] = 'A partir de 5 não reprova xD'
    
    return list

 
#Programa principal
resp = notas(5.5, 3.5, 5)
print(resp)
help(notas)