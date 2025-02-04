import sys
from tabulate import tabulate
import csv

def main():
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    if sys.argv[1] == 'regular.csv':
        header = { 'pizza': 'Regular Pizza', 'price small': 'Small', 'price large': 'Large'}
        result = table()
        print(tabulate(result, header, tablefmt='grid'))
    elif sys.argv[1] == 'sicilian.csv':
        header = { 'pizza': 'Sicilian Pizza', 'price small': 'Small', 'price large': 'Large'}
        result = table()
        print(tabulate(result, header, tablefmt='grid'))
    else:
        sys.exit('Not a CSV file')

def table():
    prices = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            if sys.argv[1] == 'regular.csv':
                prices.append({'pizza': row['Regular Pizza'], 'price small': row['Small'], 'price large': row['Large']})
            if sys.argv[1] == 'sicilian.csv':
                prices.append({'pizza': row['Sicilian Pizza'], 'price small': row['Small'], 'price large': row['Large']})

    return prices


if __name__ =='__main__':
    main()

