from datetime import date, datetime
import re
import sys
import inflect


def main():
    dob = input('Date of Birth: ',)
    if bool(re.match(r'^([0-1][0-9][0-9][0-9]|20[0-1][0-9]|202[0-3])-(0[0-9]|1[0-2])-([0-2][0-9]|3[0-1])$', dob)):
        print(convert(dob), 'minutes')
    else:
        sys.exit('Invalid date')


def convert(dob):
    p = inflect.engine()
    dob = date(int(dob[0:4]), int(dob[5:7]), int(dob[8:10]))
    today = date.today()
    #str = '2000-01-01'
    #demo = datetime.strptime(str, '%Y-%m-%d')
    diff =  today - dob
    return (p.number_to_words(diff.days * 24 * 60, andword='')).capitalize()

if __name__ == "__main__":
    main()
