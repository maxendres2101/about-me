import sys
import os
def main():
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    path = sys.argv[1]
    if path[-3:] != '.py':
        sys.exit('Not a Python file')
    if os.path.isdir(path):
        sys.exit('File does not exist')

    counter = 0
    with open(sys.argv[1]) as file:
        for line in file:
            if line.lstrip() == '':
                counter += 0
            elif line.lstrip()[0] == '#':
                counter += 0
            else:
                counter += 1

    print(counter)





if __name__ == '__main__':
    main()