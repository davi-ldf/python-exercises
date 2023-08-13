from datetime import date
atual = date.today().year
sexo = int(input('Qual seu sexo? Digite 1 para masculino e 2 para feminino: '))
if sexo == 2:
    print('Você não precisa se alistar.')
elif sexo == 1:
    nasc = int(input('Digite o ano que você nasceu: '))
    idade = atual - nasc
    if idade == 18:
        print('Se aliste IMEDIATAMENTE')
    elif idade < 18:
        saldo = 18 - idade
        print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}. Faltam {saldo} anos para seu alistamento.')
        ano = atual + saldo
        print((f'Seu alistamento será em {ano}'))
    elif idade > 18:
        saldo = idade - 18
        print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}. Já se passaram {saldo} anos do seu período de alistamento')
        ano2 = atual - saldo
        print(f'Seu alistamento foi em {ano2}')