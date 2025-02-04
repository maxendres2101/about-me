import re

def main():
    print(convert(input('Hours: ')))



def convert(hour):
    if match := re.search(r'([0-1]?[0-9])(\:[0-5][0-9])? (AM|PM) to ([0-1]?[0-9])(\:[0-5][0-9])? (AM|PM)', hour):
            if match.group(3) == 'AM' and match.group(6) == 'AM':
                if match.group(2):
                    return match.group(1) + match.group(2) + ' to ' + match.group(4) + match.group(5)
                else:
                    return match.group(1) + ':00 to ' + match.group(4) + ':00'

            if match.group(3) == 'PM' and match.group(6) == 'AM':
                if match.group(2):
                    stdClock = int(match.group(1)) + 12
                    return str(stdClock) + match.group(2) + ' to ' + match.group(4) + match.group(5)
                else:
                    stdClock = int(match.group(1)) + 12
                    return str(stdClock) + ':00 to ' + match.group(4) + ':00'

            if match.group(3) == 'AM' and match.group(6) == 'PM':
                if match.group(2):
                    stdClock = int(match.group(4)) + 12
                    return match.group(1) + match.group(2) + ' to ' + str(stdClock) + match.group(5)
                else:
                    stdClock = int(match.group(4)) + 12
                    return match.group(1) + ':00 to ' + str(stdClock) + ':00'

            if match.group(3) == 'PM' and match.group(6) == 'PM':
                if match.group(2):
                    begin = int(match.group(1)) + 12
                    end = int(match.group(4)) + 12
                    return str(begin) + match.group(2) + ' to ' + str(end) + match.group(5)
                else:
                    begin = int(match.group(1)) + 12
                    end = int(match.group(4)) + 12
                    return str(begin) + ':00 to ' + str(end) + ':00'



    else:
        raise ValueError('Wrong format')



if __name__ == '__main__':
    main()
