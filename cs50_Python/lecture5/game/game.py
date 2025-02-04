import random

def main():
    level = 1
    while True:
        try:
            level = int(input('Level: '))
            answer = random.randint(1, level)
        except ValueError:
            pass
        else:
            break

    while True:
        guess_input = input('Guess: ')
        try:
            guess = int(guess_input)
        except ValueError:
            pass
        else:
            if guess == answer:
                print('Just right!')
                break
            elif guess > answer:
                print('Too large!')
            else:
                print('Too small!')





main()