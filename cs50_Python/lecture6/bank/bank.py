def main():
    greeting = input('Enter Greeting: ')
    result = value(greeting)
    print(f'${result}')


def value(greeting):
    greeting = greeting.capitalize()
    if greeting.startswith('Hello'):
        return 0
    elif greeting.startswith('H'):
        return 20
    else:
        return 100






if __name__ == "__main__":
    main()

"""greeting = input('Enter Greeting: ')

greeting = greeting.strip()

if greeting.startswith('Hello'):
    print('$0')
elif greeting.startswith('H'):
    print('$20')
else:
    print('$100')"""



