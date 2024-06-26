import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial import Chebyshev as T
import matplotlib.animation as animation
from taylorChebLib import taylorCoeff, chebyCoeff


x = np.linspace(-1, 1, 100)  # Sample data.
cosFreq = 15

# chebyPoly = np.polynomial.chebyshev.Chebyshev()


fig, ax = plt.subplots(figsize=(15, 3), layout='constrained')
# ax.plot(x, np.cos(5*x), label='cos(5*x)')  # Plot some data on the Axes.
# ax.plot(x, x**2, label='quadratic')  # Plot more data on the Axes...
# ax.plot(x, x**3, label='cubic')  # ... and some more.
# ax.set_xlabel('x')  # Add an x-label to the Axes.
# ax.set_ylabel('f(x)')  # Add a y-label to the Axes.
ax.set(xlim=[-1, 1], ylim=[-1, 1.2], xlabel='x', ylabel='f(x)')
ax.legend()

ax.set_title("Chebyshev expansion of cosine")  # Add a title to the Axes.

# cos_full = np.full(100, 0.)
# onespace = np.full(100,1)
cosExpansionCheb = np.full(100, 0.)
cosExpansionTaylor = np.full(100, 0.)
# print(cos_taylor)
# cos_full += np.cos(5*x)

artists = []
functions_to_plot = []
functions_to_plot.append(np.cos(cosFreq*x))
ax.plot(x, functions_to_plot[0], label='cos('+str(cosFreq)+'x)')

artists=[]

maxOrder = 20
for n in range(maxOrder):
    newtermCheb = chebyCoeff(n, cosFreq).real * T.basis(n)(x)
    cosExpansionCheb += newtermCheb

    newtermTaylor = taylorCoeff(n, cosFreq) * x**n
    cosExpansionTaylor += newtermTaylor
    
    # container= ax.plot(x, cosExpansionCheb, 'r.', label= 'Tschebyscheff n = '+ str(maxOrder))
    # artists.append(container)
    # container = ax.plot(x, onespace*besselj(n, cosFreq), label= 'n = ' + str(n))
    # container = ax.plot(x, newterm, label= 'n = ' + str(n))#functions_to_plot[n], label=2*n)
    

ax.plot(x, cosExpansionCheb, 'r.', label= 'Tschebyscheff n = '+ str(maxOrder))
ax.plot(x, cosExpansionTaylor, label= 'Taylor n = '+ str(maxOrder))
ax.legend()


plt.show()