sal = int(input('How much you gain? ')) #Qual é o seu salário?
sal1 = sal + sal * 10/100
sal2 = sal + sal * 15/100
if sal > 1250:
    print(f'Who won US${sal} gonna gain US${sal1}')
else:
    print(f'Who won US${sal} gonna gain US${sal2}')
