name = input('What is your name?: ')
surname = input('Enter your surname: ')
print(f'Nice to meet you {name} {surname}!')
a = int(input('enter a: '))
b = int(input('enter b: '))

print(f'a+b={a+b}')
print(f'a-b={a-b}')
print(f'a*b={a*b}')

if b != 0:
    print(f'a/b={a/b}')
else:
    print('can not divide by 0')

