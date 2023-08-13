from datetime import date
ano = int(input('Tell me a year. Press 0 to analise the actual year: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print(f'{ano} is BISSEXT')
else:
    print(f'{ano} is NOT BISSEXT')