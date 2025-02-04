def main():
    tweet = input("Input: ")
    result = shorten(tweet)
    print(result)
    return

def shorten(tweet):
    vowels = "aeiouAEIOU"
    no_vowels = "".join(char for char in tweet if char not in vowels)
    return no_vowels



if __name__ == '__main__':
    main()