# desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos dessa ´rogressão

print('Digite o termo inicial(Número inicial), e uma razão/constante em seguida')
termo = int(input('Termo/Constante:   '))
razão = int(input('Razão:  '))
print(f'{termo}, ', end='')
for c in range(1, 10):
    termo = termo+razão
    print(f'{termo}, ', end='')
print('Fim')
0