from datetime import date
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nasc = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    atual = date.today().year
    idade = atual - nasc
    if idade >= 18:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade')
print(f'Ao todo tivemos {totmenor} pessoas menores de idade')