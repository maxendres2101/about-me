import re

def main():
    print(parse(input('HTML: ')))


def parse(link):
    if match := re.search(r"src=\"(https?)(://)(?:www\.)?(youtu)(be)\.com/embed(/xvFZjo5PgG0)\"", link, re.IGNORECASE):
        return 'https://' + match.group(3) + '.' + match.group(4) + match.group(5)
    else:
        return None







if __name__ == '__main__':
    main()
