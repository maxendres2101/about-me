def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def find_first_digit(s):
    for i in range(len(s)):
        if s[i].isdigit():
            return int(i)
    return 100


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    for i in range(2):
        if not(s[i].isalpha()):
            return False
    helper = find_first_digit(s)
    if not(helper == 100):
        if s[helper] == '0':
            return False
    if not(helper == 100):
        for i in range(helper,len(s)):
            if s[i].isalpha():
                return False

    if not(s.isalnum()):
        return False
    return True

if __name__ == '__main__':
    main()

