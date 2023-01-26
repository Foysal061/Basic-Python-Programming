# Write a program to print prime numbers from 2 to n using python range
n = int(input("Enter the maximum range: "))
for i in range(2, n+1):
    cnt = 0
    for j in range(2,i+1):
        if(i%j == 0):
            cnt = cnt + 1
    if(cnt < 2):
        print(i, " is a prime number")
    else:
        print(i, " is not a prime number")