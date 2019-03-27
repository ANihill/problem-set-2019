# Adam Nihill, 2019-03-27
# Plot of the functions x, x^2 and 2^x in the range [0, 4]

# Import matplotlip and numpy
import matplotlib.pyplot as plt 
import numpy as np

# Set range [0,4] and step of 0.2
x = np.arange(0, 4, 0.2)

# Annotations colour coded for each plot
plt.annotate("- x", xy=(4,2), xytext=(0.5, 15), color="blue", size=18)
plt.annotate("- $x^2$", xy=(4,2), xytext =(0.5, 14), color="green", size=18)
plt.annotate("- $2^x$", xy=(4,2), xytext=(0.5, 13), color="red", size=18,)

# Set parameters for each plot
plt.plot(x, x, x, x**2, x, 2**x,)
plt.show()