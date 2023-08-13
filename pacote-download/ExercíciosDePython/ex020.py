from random import shuffle
a1 = input('Primeiro nome: ')
a2 = input('Segundo nome: ')
a3 = input('Terceiro nome: ')
list = [a1, a2, a3]
shuffle(list)
print('A ordem escolhida foi {}'.format(list))



