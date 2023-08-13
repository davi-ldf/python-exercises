from time import sleep
price = float(input('Tell me the distance of a trip in km: '))
print(f'You are close to start a {price}km trip')
print('PROCESSING...')
sleep(1.5)
p1 = price * 0.50
p2 = price * 0.45
if price <= 200:
    print(f'Your trip will cost US${p1:.2f}')
else:
    print(f'Your trip will cost US${p2:.2f}')
