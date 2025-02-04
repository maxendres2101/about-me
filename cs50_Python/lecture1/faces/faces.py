def main():
    phrase = input()
    print(convert(phrase))




def convert(name):
    name = name.replace(':)', '🙂')
    name = name.replace(':(', '🙁')
    return name


main()