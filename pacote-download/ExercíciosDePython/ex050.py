soma = 0
cont = 0
for c in range(1,7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma = n + soma
        cont = cont + 1
print(f'Você informou {cont} números pares e a soma deu {soma}')
