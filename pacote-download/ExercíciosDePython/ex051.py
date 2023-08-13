#Desenvolva um programa que leia o primeiro termo
# e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
décimo = t + (11 - 1) * r
for c in range(t, décimo, r):
    print(c,'→', end= ' ')
print('ACABOU')