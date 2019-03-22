# Adam Nihill, 2019-03-22
# Prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12

# For loop for variable i in range 1000 to 10000
# Print all numbers in range that are divisible by 6 but not 12
for i in range(1000, 10000):
    if (i%6 == 0) and (i%12 != 0):
        print(i)