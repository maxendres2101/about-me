import random


def main():
    level = get_level()
    counter = 0
    score = 0
    while counter < 10:
        tries = 0
        x = generate_integer(level)
        y = generate_integer(level)
        while tries < 3:
            result = input(f"{x} + {y} = ")
            if x + y == int(result):
                score += 1
                break
            else:
                print("EEE")
                tries += 1
                if tries == 3:
                    print(f"{x} + {y} = {x+y}")
                pass
        counter += 1
    print("Score: ", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1 or level > 3:
                raise ValueError
        except ValueError:
            pass
        else:
            return int(level)


def generate_integer(level):
    x = random.randint(10 ** (level - 1), 10 ** (level) - 1)
    return x


if __name__ == "__main__":
    main()
