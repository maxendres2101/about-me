import re


def main():
    print(count(input("Text: ")))


def count(s):
    match = re.sub(r'[a-zA-Z]+um', '', s)
    match = re.sub(r'um[a-zA-Z]+', '', match)
    match = re.sub(r'[a-zA-Z]+um[a-zA-Z]+', '', match)
    match = re.findall(r'um', match, re.IGNORECASE)
    return len(match)



if __name__ == "__main__":
    main()
