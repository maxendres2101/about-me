import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    patter = r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|0?[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|0?[0-9]?[0-9])$"
    return bool(re.match(patter, ip))






if __name__ == "__main__":
    main()
