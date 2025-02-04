import sys
import os
import csv
def main():
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')

    newdict = read()
    write(newdict)

#    print(newdict[0]['First Name'])


def read():
    infos = []

    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            lastName,firstName = row['name'].split(', ')
            infos.append({'first': firstName, 'last': lastName, 'house': row['house']})
    return(infos)

def write(dict):
    with open(sys.argv[2], 'w') as file:
        writer = csv.DictWriter(file, fieldnames = ['first', 'last', 'house'])
        writer.writeheader()
        for counter in range(len(dict)):
            writer.writerow({'first': dict[counter]['first'], 'last': dict[counter]['last'], 'house': dict[counter]['house'] })
    return


if __name__ == '__main__':
    main()
