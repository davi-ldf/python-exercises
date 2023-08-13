n1 = float(input('Digite sua 1ª nota: '))
n2 = float(input('Digite sua 2ª nota: '))
media = (n1 + n2)/2
if media < 5.0:
    print(f'\033[1:31mREPROVADO. Sua média foi {media:.2f}')
elif media >= 5.0 and media < 7.0:
    print(f'\033[1:33mRECUPERAÇÃO. Sua média foi {media:.2f}')
elif media >= 7.0 and media < 10.1:
    print(f'\033[1:32mAPROVADO. Sua média foi {media:.2f}')
else:
    print('\033[1:31mTem algo de errado com essas notas.')
