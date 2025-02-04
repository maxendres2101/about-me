all = input('Enter one value then a math sign and then another value ')

all = all.split(' ')
x = all[0]

y = all[1]
z = all[2]
x = float(x)
z = float(z)

match y:
    case '+':
        print(float(x+z))
    case '-':
        print(float(x-z))
    case '*':
        print(float(x*z))
    case '/':
        print(float(x/z))