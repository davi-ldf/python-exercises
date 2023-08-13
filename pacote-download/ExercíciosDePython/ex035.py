# Programa que pede 3 retas e diz se da pra formar um triângulo com elas!!
r1 = int(input('First segment: '))
r2 = int(input('Second segment: '))
r3 = int(input('Third segment: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Da pra formar um triângulo! ;)')
else:
    print('Vai da nao')