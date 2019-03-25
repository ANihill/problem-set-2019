# Adam Nihill, 2019-03-22
# Collatz Conjecture 

# Declared variable n equal to user's input 
n = int(input("Please enter a positive integer:"))
print(n)    

# The while loop will continue until it returns an answer of one 
while n != 1:
# If n can be divided to two without a remainder it is an even number
# If it is an even number it will be divided by two 
    if (n % 2 == 0):
        n = n//2
        print(n)
# If it is an odd number it will be multiplied by three and one added to result         
    else: 
        n = (3*n) + 1
        print(n)
