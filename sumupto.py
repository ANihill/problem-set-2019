# Adam Nihill, 2019-03-17
# Input a positive integer and output the sum of all numbers between one and that number

#
sum = 0
i=1

# Set n to user's input
n = int(input("Please enter a positive integer: "))

# 
while i <= n:
    sum = sum + i
    i+=1
print(sum)
