# Write a program to find the sum of user input until users press ‘q’ from keyboard
cnt = 0
while 1:
    x = input()
    if( x == 'q' ):
        break
    cnt = cnt + int(x)
print(cnt)