n = int(input('Digite um número entre 0 e 9999: '))
n2 = str(int(10000 + n))
print('O num {} possui {} milhares'.format(n, n2[1]))
print('O num {} possui {} centenas'.format(n, n2[2]))
print('O num {} possui {} dezenas'.format(n, n2[3]))
print('O num {} possui {} unidades'.format(n, n2[4]))
