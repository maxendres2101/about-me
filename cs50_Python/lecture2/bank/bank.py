greeting = input('Enter Greeting: ')

greeting = greeting.strip()

if greeting.startswith('Hello'):
    print('$0')
elif greeting.startswith('H'):
    print('$20')
else:
    print('$100')