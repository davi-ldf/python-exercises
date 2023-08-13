from math import sin, cos, tan, radians
n = int(input('Digite um ângulo: '))
r = radians(n)
s = sin(r)
c = cos(r)
t = tan(r)
print('O seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(s, c, t))