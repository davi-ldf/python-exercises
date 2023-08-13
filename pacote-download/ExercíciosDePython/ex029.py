velocity = int(input('How many kilometers per hour do you drive? '))
if velocity <=80:
    print('VERY WELL! Keep driving safe')
else:
    multa = (velocity - 80) * 7
    print(f'WASTED!! You gonna pay US${multa},00 for this')
