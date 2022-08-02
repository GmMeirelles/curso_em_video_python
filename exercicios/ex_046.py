# faça um programa que faça uma contagem regressiva de 1 até 0 para os fogos, com o delay de 1 segundo pra cada

from time import sleep

c = 10

print("CONTAGEM REGRESSIVA PARA O LANÇAMENTO DO FOGUETE!!!!!")
sleep(2.5)
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('FOGUETE LANÇADO NA ATMOSFERA DA TERRA, PARABÉNS TRIPULANTES')