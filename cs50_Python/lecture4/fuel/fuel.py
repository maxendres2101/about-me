def main():
    fuel = input('Fraction: ').split('/')
    try:
        percent = round(int(fuel[0])/ int(fuel[1]),2) *100
    except (ValueError, ZeroDivisionError) :
        return main()

    if percent <= 1:
        print('E')
    elif int(fuel[0]) > int(fuel[1]):
        return main()
    elif percent >= 99:
        print('F')
    else:
        print(f'{int(percent)}%')




main()