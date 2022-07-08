# faça um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto

print("Bom dia! hoje estamos com um desconto de 5 porcento no produto de sua escolha")
prod = str(input("Oque deseja levar hoje?: "))
preço = int(input("Ótimo e qual o preço desse produto?: "))
desconto = preço-(preço*0.05)
print(f"Okay conforme dito um pouco acima estamos com um leve desconto e seu produto de R${preço} vai sair por R${desconto}")
input("é isso que deseja?: ")
print("Ótimo iremos realizar seu pedido agora")