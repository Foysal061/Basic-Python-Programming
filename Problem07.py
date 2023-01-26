# Write a function that will count how many vowels and consonants are present in the given string from user
def vowelCount(str):
    vowels = 0
    for i in str:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or
                i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
            vowels = vowels + 1
    return vowels


# main
str = input("Please enter a string as you wish: ")
vowels = vowelCount(str)
consonants = len(str) - vowels
print("The number of vowels:", vowels)
print("\nThe number of consonant:", consonants)
