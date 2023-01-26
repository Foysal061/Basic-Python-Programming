#Write a program to find the sum of numbers which only divisible by 5 from 1 to 100
cnt = 0
for i in range(1, 101):
    if (i % 5 == 0):
        cnt = cnt + i
print("Sum of numbers which only divisible by 5 from 1 to 100: ", cnt)
