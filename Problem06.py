# Write a function to check whether the given string from user is Palindrome or Not.
def isPalindrome(str):
    # Run loop from 0 to len/2
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True

#main

word = input("Enter a word: ")
palindrome = isPalindrome(word)
if(palindrome == True):
    print(word," is palindrome")
else:
    print(word, " is not palindrome")
