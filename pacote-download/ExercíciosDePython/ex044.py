#GERENCIADOR DE PAGAMENTOS AUTOMATIZADO
print('\033[31m==' * 10, 'LOJAS FRANÇA', '==' * 10)
price = int(input('\033[33mPreço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
paymean = int(input('Qual é a opção? \033[m'))
if paymean == 1:
    di = price - price * 10/100
    print(f'\033[35mSua compra de \033[32mR${price}\033[m será paga à vista com um desconto de 10%, custando agora \033[32mR${di}\033[m')
elif paymean == 2:
    cart = price - price * 5/100
    print(f'Sua compra de \033[32mR${price}\033[m será paga à vista no cartão com 5% de desconto, custando agora \033[32m{cart}\033[m')
elif paymean == 3:
    cart2 = price / 2
    print(f'Sua compra de \033[32mR${price}\033[m será parcelada em 2x de \033[32mR${cart2}\033[m sem juros')
elif paymean == 4:
    parc = int(input('Quantas parcelas? '))
    cart4 = price + price * 20/100
    cart3 = cart4 / parc
    print(f'Sua compra será parcelada em {parc}x de \033[32mR${cart3}\033[m \033[31mCOM JUROS\033[m\n Sua compra custará \033[32mR${cart4}\033[m no final.')