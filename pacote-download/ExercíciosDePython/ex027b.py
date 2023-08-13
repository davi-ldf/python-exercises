nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {len(n)-1}')
