from validators import email as email_validator

def main():
    email = input('What\'s your email address? ')
    if email_validator(email):
        print('Valid')
    else:
        print('Invalid')


if __name__ == '__main__':
    main()
