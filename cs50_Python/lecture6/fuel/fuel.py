def main():
    fraction = input('Fraction: ')
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    fraction = fraction.split('/')
    result = int(round ( int(fraction[0]) / int(fraction[1]),2)*100)
    if int(fraction[0]) > int(fraction[1]):
        raise ValueError
    return result

def gauge(percentage):
    if percentage <= 1:
        return('E')
    elif percentage >= 99:
        return('F')
    else:
        return(f'{int(percentage)}%')



if __name__ == '__main__':
    main()