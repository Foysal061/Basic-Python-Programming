# Print the maximum occurring character in a string.

myStr = input("Enter the string : ")

freq = {}
for i in myStr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
maxFreqChar = max(freq, key=freq.get)

print(maxFreqChar, "is the maximum frequency character with frequency of ", freq[maxFreqChar])
