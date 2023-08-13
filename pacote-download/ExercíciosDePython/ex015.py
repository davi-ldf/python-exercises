km1 = float(input('Quantos km seu veículo rodou? '))
dias1 = float(input('E por quantos dias ele foi alugado? '))
kmf = km1 * 0.15
diasf = dias1 * 60
total = kmf + diasf
print('O total a pagar pelo serviço é de R${}'.format(total))