import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from math import factorial

x = np.linspace(-1, 1, 100)  # Sample data.
cosFreq = 5



fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# ax.plot(x, np.cos(5*x), label='cos(5*x)')  # Plot some data on the Axes.
# ax.plot(x, x**2, label='quadratic')  # Plot more data on the Axes...
# ax.plot(x, x**3, label='cubic')  # ... and some more.
# ax.set_xlabel('x')  # Add an x-label to the Axes.
# ax.set_ylabel('f(x)')  # Add a y-label to the Axes.
ax.set(xlim=[-1, 1], ylim=[-1, 1.2], xlabel='x', ylabel='f(x)')
ax.legend()

ax.set_title("Taylor expansion of cosine")  # Add a title to the Axes.

# cos_full = np.full(100, 0.)
cos_taylor = np.full(100, 0.)
# print(cos_taylor)
# cos_full += np.cos(5*x)

artists = []
functions_to_plot = []
functions_to_plot.append(np.cos(cosFreq*x))
ax.plot(x, functions_to_plot[0], label='cos(5x)')

def taylorTerm(order, freq):
    return (-1)**n * (cosFreq*x)**(2*n)/factorial(2*n)

def chebyTerm(TnMinus2, TnMinus1, freq):
    return 2*freq*x*TnMinus1(x)

for n in range(3):
    newterm = taylorTerm(n, cosFreq)
    cos_taylor += newterm
    container = ax.plot(x, cos_taylor, label= 'n = ' + str(2*n))#functions_to_plot[n], label=2*n)
    ax.legend()

for n in range(3,11):
    newterm = taylorTerm(n, cosFreq)
    cos_taylor += newterm

    # functions_to_plot.append(copy.deepcopy(cos_taylor))

    # for i in range(n): 
ax.plot(x, cos_taylor, label= 'n = ' + str(20))#functions_to_plot[n], label=2*n)
ax.legend()
# ani = animation.ArtistAnimation(fig=fig, artists=artists, interval=1000)
# ani = animation.FuncAnimation(fig=fig, func=update, frames=8, interval=40)

plt.show()