# Take 5 numbers from users in a python list.
# Then find out the average number, how many even and how many odd numbers using functions: average(), countEvenNumbers(), countOddNumbers()

#Function to find average
def average(numberlist):
    sum_of_list = 0
    for i in range(len(numberlist)):
        sum_of_list += numberlist[i]
    avg = sum_of_list / len(numberlist)
    return avg

#Function to find number of even number
def countEvenNumbers(numberlist):
    cnt = 0
    for i in range(len(numberlist)):
        if(numberlist[i]%2 == 0):
            cnt = cnt+1
    return cnt

#Function to find number of even number
def countOddNumbers(numberlist):
    cnt = 0
    for i in range(len(numberlist)):
        if(numberlist[i]%2 != 0):
            cnt = cnt+1
    return cnt

#main

numbers = []
for i in range(0,5):
    x = input()
    numbers.insert(i, int(x))

print("Average: ",average(numbers))
print("Number of even numbers: ",countEvenNumbers(numbers))
print("Number of odd numbers: ",countOddNumbers(numbers))