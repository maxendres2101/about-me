import sys
from PIL import Image
import PIL
import os.path

def main():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    endingTest()
    shirt = Image.open('shirt.png')

    with Image.open(sys.argv[1]) as im:
        im = PIL.ImageOps.fit(im, (600,600))
        im.paste(shirt, (0,0), shirt)
        im.save(sys.argv[2])
    return



def endingTest():
    extensionOne = os.path.splitext(sys.argv[1])[1]
    extensionTwo = os.path.splitext(sys.argv[2])[1]


    if extensionTwo != extensionOne:
        sys.exit('Input and output have different extensions')
    elif extensionOne != '.jpg' and extensionOne != '.png' and extensionOne != '.jpeg':
        sys.exit('Invalid Input')
    elif extensionTwo != '.jpg' and extensionTwo != '.png' and extensionTwo != '.jpeg':
        sys.exit('Invalid Input')
    try:
        Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit('Input does not exist')

    return




if __name__ == '__main__':
    main()

