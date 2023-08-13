num = int(input('Tell me a int number: '))
result = num % 2 #O resto da divisão de um número par por 2 é 0; se for ímpar é 1
if result == 0:
    print(f'The number {num} is PAIR')
else:
    print(f'The number {num} is ODD')
