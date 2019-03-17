#Adam Nihill, 2019-03-17
#Function to tell if a number is prime 

# 
n = int(input("Please enter a positive integer: "))

# A prime number must be greater than 1
if n > 1:
# Prime numbers are only divisible by itself and 1
   for i in range(2,n):
       if (n % i) == 0:
           print("That is not a prime number.")
           break
   else:
       print("That is a prime number.")

else:
   print("That is not a prime number")