def main():
    name = []
    while True:
        try:
            songName = input('Name: ')
            name += [songName]
        except EOFError:
            break
    print('Adieu, adieu, to', name[0], end="")
    if len(name) == 1:
        print()
    elif len(name) == 2:
        print(' and', name[1])
    else:
        for i in range(len(name)-2):
            print(',', name[i+1], end="")
        print(', and', name[len(name)-1])









main()