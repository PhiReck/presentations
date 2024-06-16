import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial import Chebyshev as T
import matplotlib.animation as animation
from math import factorial
from special_functions import besselj

x = np.linspace(-1, 1, 100)  # Sample data.
onespace = np.full(100,1)

fig, ax = plt.subplots(1,2,figsize=(18, 6), layout='constrained')
# ax.plot(x, np.cos(5*x), label='cos(5*x)')  # Plot some data on the Axes.
# ax.plot(x, x**2, label='quadratic')  # Plot more data on the Axes...
# ax.plot(x, x**3, label='cubic')  # ... and some more.
# ax.set_xlabel('x')  # Add an x-label to the Axes.
# ax.set_ylabel('f(x)')  # Add a y-label to the Axes.
ax[0].set(xlim=[-1, 1], ylim=[-1, 1.2], xlabel='x', ylabel='x^n')
ax[1].set(xlim=[-1, 1], ylim=[-1, 1.2], xlabel='x', ylabel='T_n(x)')

ax[0].set_title("Taylor polynomials")  # Add a title to the Axes.
ax[1].set_title("Chebyshev polynomials")  # Add a title to the Axes.

for n in range(6):
    ax[0].plot(x, x**n, label= 'n = ' + str(n))#functions_to_plot[n], label=2*n)
    ax[1].plot(x, T.basis(n)(x), label= 'n = ' + str(n))#functions_to_plot[n], label=2*n)


ax[0].legend()
ax[1].legend()
plt.show()