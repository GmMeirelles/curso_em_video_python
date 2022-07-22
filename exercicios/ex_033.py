# faça um programa que leia 3 numeros e fale qual o maior e o menor

print('Digite três números:')
num1 = int(input('>>>  '))
num2 = int(input('>>>  '))
num3 = int(input('>>>  '))
num = [num1, num2, num3]

print(f'Menor: {min(num)}\nMaior: {max(num)}')