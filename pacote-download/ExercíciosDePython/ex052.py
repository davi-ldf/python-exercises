n = int(input('Digite um num: '))
tot = 0
for c in range(1, n + 1):
    if n % 1 == 0 and n % c == 0:
        print(c, end=' ')
        tot += 1
    else:
        print(f'\033[31m {c} \033[m', end= ' ')
print(f'\nO número {n} foi divisível {tot} vezes')
if tot == 2:
    print('Por isso ele \033[32mé primo')
else:
    print('Por isso ele \033[31mnão\033[m é primo')