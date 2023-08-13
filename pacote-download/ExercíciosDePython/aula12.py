# ESTRUTURAS CONDICIONAIS ANINHADAS
name = str(input('What is your name? ')).strip()
if name == 'Davi':
    print('What a wonderful name!')
elif name == 'Pedro' or name == 'Maria' or name == 'Paulo':
    print('Your name is very popular in Brazil.')
elif name in 'Ana Paula Maria Cláudia Jéssica Júlia Lara Bia':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal')
print(f'Have a good day,{name}!')
