tweet = input("Input: ")
vowels = "aeiouAEIOU"

no_vowels = "".join(char for char in tweet if char not in vowels)


print(no_vowels)
