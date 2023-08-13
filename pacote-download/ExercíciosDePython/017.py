from math import sqrt
c1 = float(input('Digite um cateto: '))
c2 = float(input('Digite outro cateto: '))
hip = (c1**2) + (c2**2)
hipf = sqrt(hip)
print('A hipotenusa é {}'.format(hipf))