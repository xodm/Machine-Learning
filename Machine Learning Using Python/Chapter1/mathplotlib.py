%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
# Generate a sequence of numbers from -10 to 10 with 100 steps in between
x = np.linspace(-10, 10, 100)
#Makes the x-axis 
# Create a second array using sine
y = np.sin(x)
#Makes the function in terms of the x's
# The plot function makes a line chart of one array against another
plt.plot(x, y, marker="x")