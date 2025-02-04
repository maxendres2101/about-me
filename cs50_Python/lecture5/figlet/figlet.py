import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

if len(sys.argv) == 1:
    rand = random.randint(0,549)
    font = figlet.getFonts()[rand]
    figlet.setFont(font = font)
    text = input('Input: ')
    print (figlet.renderText(text))
elif len(sys.argv) == 3:
    if not(sys.argv[1] == '-f') and not(sys.argv[1] == '--font'):
        sys.exit('Invalid usage')
    else:
        figlet.setFont(font = sys.argv[2])
        #print(sys.argv[0], sys.argv[1], sys.argv[2])
        text = input('Input: ')
        print (figlet.renderText(text))
else:
    sys.exit('Invalid usage')




'''
font = figlet.getFonts()[2]
print(font)
'''