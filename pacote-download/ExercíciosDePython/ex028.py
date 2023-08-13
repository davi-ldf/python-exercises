from random import randint
from time import sleep
print('=--=' * 20) #Decorative
print('Vou pensar em um número de 0 a 5, tente adivinhar!')
print('=--=' * 20) #Decorative
player = int(input('Em que número eu pensei? ')) # Player try's to win
machine = randint(0, 5) # Make the machine "THINK"
print('PROCESSANDO...')
sleep(2)
if player == machine:
    print(f'Acertou, pensei no número {machine}')
else:
    print(f'Errou, pensei no número {machine}')
print('=--=' * 20) #Decorative
