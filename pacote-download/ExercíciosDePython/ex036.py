house = int(input('What´s the price of the house in dollars? '))
wage = int(input('Your wage in dollars: '))
years = int(input('How many years you gonna take to pay? '))
parcela = house/(years*12) #Cálculo do valor da parcela da casa
wagemax = wage * 30/100 #Cálculo de 30% do salário (não pode exceder)
print('\033[35m=-=-='*10) #Decoração
if parcela >= wagemax:
    print('\033[31mSorry,\033[m you are \033[31mnot\033[m able to pay for this house.')
elif parcela < wagemax:
    print(f'\033[32mNice!\033[m You gonna pay US${parcela:.2f} per month for \033[33m{years} years\033[m to own a US${house}.00 house')
