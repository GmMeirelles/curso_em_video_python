#algumas das funções extras mostradas foram \n usado para quebrar a linha no meio de um print e end=" " para fazer o print da linha de baixo se juntar a mesma linha

print("Aqui vai separar a linha: \ne esta parte ficara em outra linha\n--------------------------")
print("aqui começa o e termina o primeiro print: ", end='')
print("aqui começa outro print que vai ser juntado a linha de cima")
print("----------------------------------------------")
#se quiser definir em quantas letras vai poder ser escrito oq tu quer dentro da chave basta colocar {:20}, o python vai colocar 20 espaçõs e colocar oq tem na variavel entre eles

nome = str(input("digite seu nome: "))
print("Bom dia {:20} Tudo bem?" .format(nome))

# se quiser substituir os espaços por algum caracter use {:=20}, e para alinhar use < para a variavel ficar a esquerda dos caracteres, > para a direita e ^ para centralizar

print("Bom dia {:=^20} Tudo bem?" .format(nome))