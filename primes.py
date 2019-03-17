n = int(input("Please enter a positive integer: "))

if n > 1:
   for i in range(2,n):
       if (n % i) == 0:
           print("That is not a prime number.")
           break
   else:
       print("That is a prime number.")

else:
   print("That is not a prime number")