from random import randint
from time import sleep
print('=--=' * 20) #Decorative
print('PEDRA, PAPEL E TESOURA')
print('=--=' * 20) #Decorative
print('''
[0] ROCK/PEDRA
[1] PAPER/PAPEL
[2] SCISSORS/TESOURA''')
r = str('rock')
p = str('paper')
s = str('scissors')
ppt = int(input('Qual sua jogada?: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2) # Make the machine "CHOOSE"
print('-=' * 10)
print(f'JOGADOR JOGOU {itens[ppt]}')
print(f'COMPUTADOR JOGOU {itens[pc]}')
print('-=' * 10)
if ppt == 0 and pc == 1:
    print('COMPUTADOR VENCE')
elif ppt == 0 and pc == 2:
    print('JOGADOR VENCE')
elif ppt == 1 and pc == 0:
    print('JOGADOR VENCE')
elif ppt == 1 and pc == 2:
    print('COMPUTADOR VENCE')
elif ppt == 2 and pc == 0:
    print('COMPUTADOR VENCE')
elif ppt == 2 and pc == 1:
    print('JOGADOR VENCE')
elif ppt == pc:
    print('No winner')
else:
    print('Invalid answer.')