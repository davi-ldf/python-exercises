a = int(input('First number: '))
b = int(input('Second number: '))
c = int(input('Third number: '))
#Verificando quem é menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#Verificando quem é o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'The bigger number is {maior} ')
print(f'The shorter number is {menor} ')