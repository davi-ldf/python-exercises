num = int(input('Disk a number: '))
print('''Choice one of the bases to convert
[1] Binary
[2] Octal
[3] Hexadecimal''')
choice = int(input(': '))
if choice == 1:
    print(f'The number {num} converted to Binary is {bin(num)[2:]}')
elif choice == 2:
    print(f'The number {num} converted to Octal is {oct(num)[2:]}')
elif choice == 3:
    print(f'The number {num} converted to Hexadecimal is {hex(num)[2:]}')
else:
    print('\033[31mUnavaliable option. Try again.')