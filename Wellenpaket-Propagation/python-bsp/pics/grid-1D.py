import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial import Chebyshev as T
import matplotlib.animation as animation
from math import factorial
from special_functions import besselj

xlimit = 2.2

x = np.linspace(-xlimit, xlimit, 50)  # Sample data.
cosFreq = 15

# chebyPoly = np.polynomial.chebyshev.Chebyshev()

plt.rcParams.update({'font.size': 22})
fig, ax = plt.subplots(figsize=(12, 10), layout='constrained')
# ax.plot(x, np.cos(5*x), label='cos(5*x)')  # Plot some data on the Axes.
# ax.plot(x, x**2, label='quadratic')  # Plot more data on the Axes...
# ax.plot(x, x**3, label='cubic')  # ... and some more.
# ax.set_xlabel('x')  # Add an x-label to the Axes.
# ax.set_ylabel('f(x)')  # Add a y-label to the Axes.
ax.set(xlim=[-xlimit, xlimit], ylim=[0, 1.2], xlabel='x', ylabel='f(x)')

ax.set_title("Function on grid")  # Add a title to the Axes.

expon = np.exp(-x*x)

ax.plot(x, expon, label='$e^{-x^2}$', linewidth = 3)
legends = ax.legend(fontsize = 30)
fig.savefig("/mnt/c/Users/qayws/Documents/Physik/presentations/TH-Ohm-Numerik/Wellenpaket-Propagation/pictures/function_no_grid_auto.png")


ax.plot(x, expon, 'r.', label='on grid', markersize = 20)
legends = ax.legend(fontsize = 30)
fig.savefig("/mnt/c/Users/qayws/Documents/Physik/presentations/TH-Ohm-Numerik/Wellenpaket-Propagation/pictures/function_on_grid_auto.png")
# help(legends)

plt.show()
