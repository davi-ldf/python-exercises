valor = float(input('Qual era o preço inicial do produto? R$'))
desc = valor-valor*(5/100)
juro = valor+(valor*5/100)
print('O produto à vista tem desconto de 5%, custando R${:.2f} e a prazo custa {}'.format(desc, juro))
