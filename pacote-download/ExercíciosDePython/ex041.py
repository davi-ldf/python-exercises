from datetime import date
year = date.today().year
born = int(input('Digite o ano em que nasceu: '))
age = year - born
if age < 10:
    print('Atleta MIRIM')
elif age < 15:
    print('Atleta INFANTIL')
elif age < 20:
    print('Atleta JUNIOR')
elif age < 26:
    print('Atleta SÊNIOR')
else:
    print('Atleta MASTER')
