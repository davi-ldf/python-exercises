#Qual número é o maior? (Estruturas Aninhadas [AULA 12])
num = int(input('Disk a int number: '))
num2 = int(input('Disk other number: '))
if num > num2:
    print('The FIRST number is bigger')
elif num < num2:
    print('The SECOND number is bigger')
elif num == num2:
    print('There´s \033[31mNOT\033[m a bigger number, they´re the same.')

