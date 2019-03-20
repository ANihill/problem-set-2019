# Adam Nihill, 2019-03-17
# Input a positive integer and output the sum of all numbers between one and that number

# Created a variable "sum" containing the integer 0
sum = 0
# Variable "I" contains the integer
i=1

# Created a variable "n" which contains user's input
n = int(input("Please enter a positive integer: "))

# Adds sum to i, storing result in variable i
while i <= n:
    sum = sum + i
    i+=1
print(sum)
