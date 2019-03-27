# Adam Nihill, 2019-03-25

rootof = float(input("Please enter a number: "))

# estimate = float(input("Please enter an initial estimate for the square root: "))
# Commented out input for initial estimate and set to 10
estimate = 10

# While the difference between estimate squared minus rootof is greater that 0.001 loop will continue
# Divide estimate squared minus rootof by two times estimate
while abs((estimate * estimate) - rootof) > 0.001:
    estimate -= ((estimate * estimate) - rootof)/(2 * estimate)

print(f"The square root of {rootof} is approx {estimate}.")