import random
p = input('First student: ')
s = input('Second student: ')
t = input('Third student: ')
list = [p, s, t]
choiced = random.choice(list)
print('The selected student was {}'.format(choiced))